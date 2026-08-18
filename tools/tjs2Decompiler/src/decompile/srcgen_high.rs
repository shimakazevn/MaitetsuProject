use anyhow::Result;
use std::collections::{HashMap, HashSet};
use std::fmt::Write as _;

use crate::{Tjs2File, Tjs2Object};

use super::cfg::Cfg;
use super::expr::{BinOp, Expr, UnOp};
use super::expr_build::{ExprProgram, Stmt, Terminator};
use super::ssa::{SsaProgram, Var, VarId};

fn vm_binop(op: &str) -> Option<BinOp> {
    match op {
        "VM_ADD" | "ADD" => Some(BinOp::Add),
        "VM_SUB" | "SUB" => Some(BinOp::Sub),
        "VM_MUL" | "MUL" => Some(BinOp::Mul),
        "VM_DIV" | "DIV" => Some(BinOp::Div),
        "VM_MOD" | "MOD" => Some(BinOp::Mod),

        "VM_SAL" | "SHL" => Some(BinOp::Shl),
        "VM_SAR" | "SHR" => Some(BinOp::Shr),
        "VM_SR" | "USHR" => Some(BinOp::UShr),

        "VM_BAND" | "BAND" => Some(BinOp::BitAnd),
        "VM_BXOR" | "BXOR" => Some(BinOp::BitXor),
        "VM_BOR" | "BOR" => Some(BinOp::BitOr),

        "VM_LAND" | "LAND" => Some(BinOp::LogAnd),
        "VM_LOR" | "LOR" => Some(BinOp::LogOr),

        "VM_EQ" | "EQ" => Some(BinOp::Eq),
        "VM_NE" | "NE" => Some(BinOp::Ne),
        "VM_DEQ" | "DEQ" => Some(BinOp::StrictEq),
        "VM_DNE" | "DNE" => Some(BinOp::StrictNe),

        "VM_LT" | "LT" => Some(BinOp::Lt),
        "VM_LE" | "LE" => Some(BinOp::Le),
        "VM_GT" | "GT" => Some(BinOp::Gt),
        "VM_GE" | "GE" => Some(BinOp::Ge),

        "VM_IN" | "CHKINS" => Some(BinOp::In),

        _ => None,
    }
}

fn vm_unop(op: &str) -> Option<UnOp> {
    match op {
        "VM_CHS" | "CHS" => Some(UnOp::Neg),
        "VM_LNOT" | "LNOT" => Some(UnOp::Not),
        "VM_BNOT" | "BNOT" => Some(UnOp::BitNot),
        "VM_TYPEOF" | "TYPEOF" => Some(UnOp::Typeof),
        "VM_DELETE" | "DELETE" => Some(UnOp::Delete),
        _ => None,
    }
}

fn fmt_octet_literal(bytes: &[u8]) -> String {
    // B: official usage style
    let mut s = String::new();
    s.push_str("octet([");
    for (k, b) in bytes.iter().enumerate() {
        if k != 0 {
            s.push_str(", ");
        }
        s.push_str(&format!("0x{:02X}", b));
    }
    s.push_str("])");
    s
}

fn escape_tjs_string_min(s: &str) -> String {
    let mut out = String::new();
    for ch in s.chars() {
        match ch {
            '\\' => out.push_str("\\\\"),
            '"' => out.push_str("\\\""),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            '\0' => out.push_str("\\0"),
            _ => out.push(ch),
        }
    }
    out
}

/// Options controlling how code is emitted.
pub struct SrcgenOptions {
    pub inline: bool,
}

impl Default for SrcgenOptions {
    fn default() -> Self {
        SrcgenOptions { inline: true }
    }
}

/// Returns true if obj or any of its ancestors (via parent chain) is a class (context_type=6),
/// stopping at context_type=0 (global). Used to decide if `%-2` (scope) maps to `this`.
fn scope_is_class(file: &Tjs2File, obj: &Tjs2Object) -> bool {
    let mut cur = obj.parent;
    loop {
        if cur < 0 || cur as usize >= file.objects.len() {
            return false;
        }
        let p = &file.objects[cur as usize];
        match p.context_type {
            0 => return false,
            6 => return true,
            _ => cur = p.parent,
        }
    }
}

/// Build a fmt_var closure appropriate for the given object's context.
/// - r >= 0: r{r}_{ver}
/// - r == -1: "this"
/// - r == -2: "this" if in a class scope, else "global"
/// - r <= -3 and frame_idx < arg_count: "a{frame_idx}" (declared parameter)
/// - r <= -3 and frame_idx >= arg_count: "_fr{frame_idx - arg_count}" (local frame slot)
fn make_fmt_var(in_class: bool, arg_count: usize) -> impl Fn(VarId) -> String {
    move |vid: VarId| -> String {
        match vid.var {
            Var::Reg(r) if r >= 0 => format!("r{}_{}", r, vid.ver),
            Var::Reg(-1) => "this".to_string(),
            Var::Reg(-2) => {
                if in_class {
                    "this".to_string()
                } else {
                    "global".to_string()
                }
            }
            Var::Reg(r) => {
                let frame_idx = (-3 - r) as usize;
                if frame_idx < arg_count {
                    format!("a{}", frame_idx)
                } else {
                    format!("_fr{}", frame_idx - arg_count)
                }
            }
            Var::Flag => format!("flag_{}", vid.ver),
            Var::Exception => format!("exc_{}", vid.ver),
        }
    }
}

// pub fn dump_src_file(file: &Tjs2File, _opt: SrcgenOptions) -> Result<String> {
//     let mut out = String::new();
//     writeln!(
//         out,
//         "// Decompiled from TJS2 bytecode\n// objects: {}\n",
//         file.objects.len()
//     )?;

//     for obj in &file.objects {
//         if obj.code.is_empty() {
//             continue;
//         }
//         writeln!(
//             out,
//             "// == object {}: {} ==",
//             obj.index,
//             obj.name.as_deref().unwrap_or("<anonymous>")
//         )?;

//         let lhs = obj_lhs(obj.index, obj.name.as_deref());
//         writeln!(out, "{} = function() {{", lhs)?;

//         let cfg = Cfg::build(obj)?;
//         let ssa = SsaProgram::from_cfg(&cfg)?;
//         let prog = ExprProgram::from_ssa(file, obj, &ssa)?;

//         let fmt_var = |vid: VarId| -> String { fmt_vid_tjs(vid) };
//         emit_var_decls(&mut out, &prog, &fmt_var)?;

//         // Recover return expressions from SSA (expr_build's Terminator::Ret has no expr).
//         let mut ret_expr: Vec<Option<Expr>> = vec![None; prog.blocks.len()];
//         for b in &ssa.blocks {
//             if let Some(last) = b.insns.last() {
//                 // VM_RET has the return value in uses[0] (static, no guessing).
//                 if last.mnemonic.eq_ignore_ascii_case("RET") || last.mnemonic.eq_ignore_ascii_case("VM_RET") {
//                     if let Some(v) = last.uses.get(0).copied() {
//                         ret_expr[b.id] = Some(Expr::SsaVar(v));
//                     }
//                 }
//             }
//         }

//         let mut s = Structurer::new(&cfg, &prog, &fmt_var, ret_expr);
//         let lines = s.emit_function_body(prog.entry_block, 2);

//         for l in lines {
//             writeln!(out, "{}", l)?;
//         }
//         writeln!(out, "}};\n")?;
//     }

//     Ok(out)
// }

fn const_propagate_intrablock(prog: &mut ExprProgram) {
    // In TJS2, the initial value (ver=0) of all non-negative local registers is void.
    // Register 0 (result register) is most commonly seen as "void" when used as a store value.
    let initial_void: HashMap<VarId, Expr> = {
        let mut m = HashMap::new();
        m.insert(
            VarId {
                var: Var::Reg(0),
                ver: 0,
            },
            Expr::Void,
        );
        m
    };

    for b in &mut prog.blocks {
        let mut env: HashMap<VarId, Expr> = initial_void.clone();

        for st in &mut b.stmts {
            // 1) rewrite uses in this statement
            rewrite_stmt(st, &env);

            // 2) record defs if RHS is safe to propagate
            match st {
                Stmt::Assign { dst, expr } => {
                    if let Some(v) = prop_value(expr, &env) {
                        env.insert(*dst, v);
                    }
                }
                // Opaque: only propagate if you have explicit “pure” ones (optional)
                Stmt::Opaque { defs, op, args } => {
                    // keep simple: do not record (safe default)
                    let _ = (defs, op, args);
                }
                _ => {}
            }
        }
    }
}

fn rewrite_stmt(st: &mut Stmt, env: &HashMap<VarId, Expr>) {
    match st {
        Stmt::Assign { expr, .. } => rewrite_expr(expr, env),
        Stmt::Store { target, value } => {
            rewrite_expr(target, env);
            rewrite_expr(value, env);
        }
        Stmt::Update { target, rhs, .. } => {
            rewrite_expr(target, env);
            rewrite_expr(rhs, env);
        }
        Stmt::Expr(e) => rewrite_expr(e, env),
        Stmt::Opaque { args, .. } => {
            for a in args {
                rewrite_expr(a, env);
            }
        }
    }
}

fn rewrite_expr(e: &mut Expr, env: &HashMap<VarId, Expr>) {
    match e {
        Expr::SsaVar(v) => {
            if let Some(rep) = env.get(v).cloned() {
                *e = rep;
            }
        }
        Expr::Unary(_, expr) => rewrite_expr(expr, env),
        Expr::Binary(_, lhs, rhs) => {
            rewrite_expr(lhs, env);
            rewrite_expr(rhs, env);
        }
        Expr::Member(base, _) | Expr::Deref(base) => rewrite_expr(base, env),
        Expr::Index(base, index) => {
            rewrite_expr(base, env);
            rewrite_expr(index, env);
        }
        Expr::Call(callee, args) => {
            rewrite_expr(callee, env);
            for a in args {
                rewrite_expr(a, env);
            }
        }
        Expr::New(ctor, args) => {
            rewrite_expr(ctor, env);
            for a in args {
                rewrite_expr(a, env);
            }
        }
        Expr::MethodCall { base, args, .. } => {
            rewrite_expr(base, env);
            for a in args {
                rewrite_expr(a, env);
            }
        }
        Expr::Opaque(_, args) => {
            for a in args {
                rewrite_expr(a, env);
            }
        }
        _ => {}
    }
}

/// Decide whether `rhs` is safe to propagate as a value.
/// Keep it conservative: literals, variable aliases, and global/thisproxy member refs.
fn prop_value(rhs: &Expr, env: &HashMap<VarId, Expr>) -> Option<Expr> {
    let mut v = rhs.clone();
    rewrite_expr(&mut v, env);

    match &v {
        // literals
        Expr::Void
        | Expr::Null
        | Expr::Bool(_)
        | Expr::Int(_)
        | Expr::Real(_)
        | Expr::Str(_)
        | Expr::Octet(_) => Some(v),

        // alias
        Expr::SsaVar(_) => Some(v),

        // member ref: allow base to be global/thisproxy/this or an already-propagated alias
        Expr::Member(base, name) => {
            let ok = matches!(
                **base,
                Expr::SsaVar(VarId {
                    var: Var::Reg(-2),
                    ..
                }) | Expr::SsaVar(VarId {
                    var: Var::Reg(-1),
                    ..
                }) // this
            ) || is_identifier(name);
            if ok { Some(v) } else { None }
        }

        _ => None,
    }
}

fn emit_object_body(obj: &Tjs2Object, file: &Tjs2File, indent: usize) -> Result<(String, String)> {
    let mut out = String::new();

    let cfg = Cfg::build(obj)?;
    let ssa = SsaProgram::from_cfg(&cfg)?;
    let mut prog = ExprProgram::from_ssa(file, obj, &ssa)?;
    const_propagate_intrablock(&mut prog);

    let params = build_params(obj);
    let arg_count = obj.func_decl_arg_count.max(0) as usize;

    let in_class = scope_is_class(file, obj);
    let fmt_var = make_fmt_var(in_class, arg_count);

    // Recover return value from SSA: find the SRV source (it writes to r0 conceptually).
    // We special-case: for SRV opaque stmts, propagate the arg into a synthetic ret_expr.
    let mut ret_expr: Vec<Option<Expr>> = vec![None; prog.blocks.len()];
    for b in &ssa.blocks {
        // Find the last SRV instruction in this block and use its source as ret_expr.
        let srv = b.insns.iter().rev().find(|i| {
            i.mnemonic.eq_ignore_ascii_case("SRV") || i.mnemonic.eq_ignore_ascii_case("VM_SRV")
        });
        if let Some(si) = srv {
            if let Some(v) = si.uses.get(0).copied() {
                ret_expr[b.id] = Some(Expr::SsaVar(v));
            }
        }
    }
    propagate_into_ret_expr(&mut ret_expr, &prog);
    remove_dead_phis(&mut prog, &ret_expr);
    remove_dead_assigns(&mut prog, &ret_expr);

    emit_var_decls(&mut out, &prog, &fmt_var, arg_count, indent)?;

    let mut s = Structurer::new(&cfg, &prog, &fmt_var, ret_expr);
    let lines = s.emit_function_body(prog.entry_block, indent);

    for l in lines {
        writeln!(out, "{}", l)?;
    }
    Ok((out, params))
}

/// Build param string from func_decl_arg_count (authoritative — always trust it).
fn build_params(obj: &Tjs2Object) -> String {
    let n = obj.func_decl_arg_count.max(0) as usize;
    (0..n)
        .map(|i| format!("a{}", i))
        .collect::<Vec<_>>()
        .join(", ")
}

/// Propagate constant assignments into ret_expr for each block.
fn propagate_into_ret_expr(ret_expr: &mut Vec<Option<Expr>>, prog: &ExprProgram) {
    for b in &prog.blocks {
        let Some(re) = ret_expr.get_mut(b.id) else {
            continue;
        };
        let Some(e) = re else {
            continue;
        };
        let mut env: HashMap<VarId, Expr> = HashMap::new();
        for st in &b.stmts {
            match st {
                Stmt::Assign { dst, expr } => {
                    let mut v = expr.clone();
                    rewrite_expr(&mut v, &env);
                    if let Some(pv) = prop_value(&v, &env) {
                        env.insert(*dst, pv);
                    }
                }
                Stmt::Opaque { op, args, defs }
                    if (op.eq_ignore_ascii_case("VM_SRV") || op.eq_ignore_ascii_case("SRV"))
                        && !args.is_empty()
                        && !defs.is_empty() =>
                {
                    let mut v = args[0].clone();
                    rewrite_expr(&mut v, &env);
                    if let Some(pv) = prop_value(&v, &env) {
                        env.insert(defs[0], pv);
                    }
                }
                _ => {}
            }
        }
        rewrite_expr(e, &env);
    }
}

/// Eliminate phi nodes whose results are never truly used (i.e. only consumed by other dead
/// phis or by edge copies that feed dead phis).  After this pass, `build_edge_copies` will
/// not emit the now-removed phi copies, and a subsequent `remove_dead_assigns` will clean up
/// any statements that only computed values for those dead phi args.
fn remove_dead_phis(prog: &mut ExprProgram, ret_expr: &[Option<Expr>]) {
    // Phase 1 – seed: vars used in stmts / terminators / ret_expr (NOT phi args yet).
    let mut live: HashSet<VarId> = HashSet::new();
    for b in &prog.blocks {
        for st in &b.stmts {
            collect_uses_stmt(st, &mut live);
        }
        collect_vars_term(&b.term, &mut live);
    }
    for re in ret_expr {
        if let Some(e) = re {
            collect_vars_expr(e, &mut live);
        }
    }

    // Phase 2 – propagate: if a phi result is live, its args become live.
    let mut changed = true;
    while changed {
        changed = false;
        for b in &prog.blocks {
            for phi in &b.phi {
                if live.contains(&phi.result) {
                    for (_, v) in &phi.args {
                        if live.insert(*v) {
                            changed = true;
                        }
                    }
                }
            }
        }
    }

    // Phase 3 – prune: drop every phi whose result is not in the live set.
    for b in &mut prog.blocks {
        b.phi.retain(|phi| live.contains(&phi.result));
    }
}

/// Remove Assign statements whose dst is never referenced anywhere after constant propagation.
fn remove_dead_assigns(prog: &mut ExprProgram, ret_expr: &[Option<Expr>]) {
    let mut used: HashSet<VarId> = HashSet::new();
    for b in &prog.blocks {
        for phi in &b.phi {
            for (_, v) in &phi.args {
                used.insert(*v);
            }
        }
        for st in &b.stmts {
            collect_uses_stmt(st, &mut used); // only RHS / side-effect reads, not dsts
        }
        collect_vars_term(&b.term, &mut used);
    }
    for re in ret_expr {
        if let Some(e) = re {
            collect_vars_expr(e, &mut used);
        }
    }

    let mut dead_dsts: HashSet<VarId> = HashSet::new();
    for b in &prog.blocks {
        for st in &b.stmts {
            if let Stmt::Assign { dst, .. } = st {
                if !used.contains(dst) {
                    dead_dsts.insert(*dst);
                }
            }
        }
    }
    for b in &mut prog.blocks {
        b.stmts
            .retain(|st| !matches!(st, Stmt::Assign { dst, .. } if dead_dsts.contains(dst)));
    }
}

/// Collect only the "use" side of a statement (not defs of Assign).
fn collect_uses_stmt(st: &Stmt, s: &mut HashSet<VarId>) {
    match st {
        Stmt::Assign { expr, .. } => collect_vars_expr(expr, s), // dst is a def, skip it
        Stmt::Store { target, value } => {
            collect_vars_expr(target, s);
            collect_vars_expr(value, s);
        }
        Stmt::Update {
            dst, target, rhs, ..
        } => {
            if let Some(d) = dst {
                s.insert(*d); // the update result is a use-def; still mark it used
            }
            collect_vars_expr(target, s);
            collect_vars_expr(rhs, s);
        }
        Stmt::Expr(e) => collect_vars_expr(e, s),
        Stmt::Opaque { args, defs, .. } => {
            for d in defs {
                s.insert(*d);
            }
            for a in args {
                collect_vars_expr(a, s);
            }
        }
    }
}

fn infer_single_return_expr(file: &Tjs2File, getter_obj: &Tjs2Object) -> Option<String> {
    let cfg = Cfg::build(getter_obj).ok()?;
    let ssa = SsaProgram::from_cfg(&cfg).ok()?;
    let mut prog = ExprProgram::from_ssa(file, getter_obj, &ssa).ok()?;
    const_propagate_intrablock(&mut prog);

    let in_class = scope_is_class(file, getter_obj);
    let arg_count = getter_obj.func_decl_arg_count.max(0) as usize;
    let fmt_var = make_fmt_var(in_class, arg_count);

    // Collect SRV return expressions
    let mut ret_expr: Vec<Option<Expr>> = vec![None; prog.blocks.len()];
    for b in &ssa.blocks {
        let srv = b.insns.iter().rev().find(|i| {
            i.mnemonic.eq_ignore_ascii_case("SRV") || i.mnemonic.eq_ignore_ascii_case("VM_SRV")
        });
        if let Some(si) = srv {
            if let Some(v) = si.uses.get(0).copied() {
                ret_expr[b.id] = Some(Expr::SsaVar(v));
            }
        }
    }
    propagate_into_ret_expr(&mut ret_expr, &prog);

    let mut unique_ret: Option<String> = None;
    for re in &ret_expr {
        if let Some(e) = re {
            let s = e.to_tjs_with(&fmt_var);
            if let Some(prev) = &unique_ret {
                if *prev != s {
                    return None;
                }
            } else {
                unique_ret = Some(s);
            }
        }
    }
    unique_ret
}

pub fn dump_src_file(file: &Tjs2File) -> Result<String> {
    let mut out = String::new();
    writeln!(out, "// Decompiled by tjs2Decompiler (high)")?;
    writeln!(
        out,
        "// objects={}, toplevel={}",
        file.objects.len(),
        file.toplevel
    )?;
    writeln!(out)?;

    let toplevel = file.toplevel.max(0) as usize;

    // Build parent -> children index (ordered by object index)
    let mut children_of: HashMap<usize, Vec<usize>> = HashMap::new();
    for obj in &file.objects {
        if obj.parent >= 0 {
            children_of
                .entry(obj.parent as usize)
                .or_default()
                .push(obj.index);
        }
    }

    // Track emitted objects to avoid duplication
    let mut emitted: HashSet<usize> = HashSet::new();
    emitted.insert(toplevel);

    // === Emit classes: context_type==6 with parent==toplevel ===
    let classes: Vec<usize> = file
        .objects
        .iter()
        .filter(|o| o.context_type == 6 && o.parent == toplevel as i32)
        .map(|o| o.index)
        .collect();

    for cls_idx in classes {
        let cls_obj = &file.objects[cls_idx];
        let cls_name = match cls_obj.name.as_deref() {
            Some(n) if is_identifier(n) => n.to_string(),
            _ => format!("__class_{}", cls_idx),
        };

        emitted.insert(cls_idx);

        // extends: use super_class_getter field, or find context_type==7 child
        let extends = if cls_obj.super_class_getter >= 0 {
            let sg = cls_obj.super_class_getter as usize;
            if sg < file.objects.len() {
                emitted.insert(sg);
                infer_single_return_expr(file, &file.objects[sg])
            } else {
                None
            }
        } else {
            // fallback: look for context_type==7 child
            children_of
                .get(&cls_idx)
                .and_then(|ch| ch.iter().find(|&&ci| file.objects[ci].context_type == 7))
                .and_then(|&ci| {
                    emitted.insert(ci);
                    infer_single_return_expr(file, &file.objects[ci])
                })
        };

        match &extends {
            Some(e) => writeln!(out, "class {} extends {} {{", cls_name, e)?,
            None => writeln!(out, "class {} {{", cls_name)?,
        }

        let empty_children: Vec<usize> = Vec::new();
        let children = children_of.get(&cls_idx).unwrap_or(&empty_children).clone();

        let mut first_member = true;
        for ci in &children {
            if emitted.contains(ci) {
                continue;
            }
            let mobj = &file.objects[*ci];
            match mobj.context_type {
                7 => {
                    emitted.insert(*ci);
                } // superclass getter already handled
                2 => {
                    emitted.insert(*ci);
                } // anonymous closure – skip top-level
                3 => {
                    // Property object
                    emitted.insert(*ci);
                    let prop_name = match mobj.name.as_deref() {
                        Some(n) if n != "(anonymous)" && is_identifier(n) => n.to_string(),
                        _ => format!("__prop_{}", ci),
                    };
                    if !first_member {
                        writeln!(out)?;
                    }
                    first_member = false;
                    writeln!(out, "  property {} {{", prop_name)?;

                    if mobj.prop_getter >= 0 {
                        let gi = mobj.prop_getter as usize;
                        if gi < file.objects.len() && !emitted.contains(&gi) {
                            // body indent=6: class(2) + property(2) + getter(2)
                            let (body, _params) = emit_object_body(&file.objects[gi], file, 6)?;
                            writeln!(out, "    getter() {{")?;
                            write!(out, "{body}")?;
                            writeln!(out, "    }}")?;
                            emitted.insert(gi);
                        }
                    }
                    if mobj.prop_setter >= 0 {
                        let si = mobj.prop_setter as usize;
                        if si < file.objects.len() && !emitted.contains(&si) {
                            // body indent=6: class(2) + property(2) + setter(2)
                            let (body, params) = emit_object_body(&file.objects[si], file, 6)?;
                            writeln!(out, "    setter({}) {{", params)?;
                            write!(out, "{body}")?;
                            writeln!(out, "    }}")?;
                            emitted.insert(si);
                        }
                    }

                    // Mark any context_type==5 (getter) children of the property object
                    if let Some(prop_children) = children_of.get(ci) {
                        for &pci in prop_children {
                            emitted.insert(pci);
                        }
                    }

                    writeln!(out, "  }}")?;
                }
                1 => {
                    // Method
                    let mname = match mobj.name.as_deref() {
                        Some(n) if n != "(anonymous)" && is_identifier(n) => n.to_string(),
                        _ => format!("__method_{}", ci),
                    };
                    emitted.insert(*ci);
                    // Mark anonymous children (closures inside this method)
                    if let Some(mch) = children_of.get(ci) {
                        for &mci in mch {
                            if file.objects[mci].context_type == 2 {
                                emitted.insert(mci);
                            }
                        }
                    }

                    if !first_member {
                        writeln!(out)?;
                    }
                    first_member = false;

                    if mobj.code.is_empty() {
                        writeln!(out, "  function {}() {{}}", mname)?;
                    } else {
                        // body indent=4: class(2) + method(2)
                        let (body, params) = emit_object_body(mobj, file, 4)?;
                        writeln!(out, "  function {}({}) {{", mname, params)?;
                        write!(out, "{body}")?;
                        writeln!(out, "  }}")?;
                    }
                }
                _ => {
                    emitted.insert(*ci);
                }
            }
        }

        writeln!(out, "}}")?;
        writeln!(out)?;
    }

    // === Emit top-level functions: context_type==1 with parent==toplevel ===
    for obj in &file.objects {
        if emitted.contains(&obj.index) {
            continue;
        }
        if obj.parent != toplevel as i32 {
            continue;
        }
        if obj.context_type != 1 {
            continue;
        }
        if obj.code.is_empty() {
            continue;
        }

        let name = match obj.name.as_deref() {
            Some(n) if n != "(anonymous)" && is_identifier(n) => n.to_string(),
            _ => format!("__func_{}", obj.index),
        };
        emitted.insert(obj.index);

        // Mark anonymous closure children
        if let Some(ch) = children_of.get(&obj.index) {
            for &ci in ch {
                if file.objects[ci].context_type == 2 {
                    emitted.insert(ci);
                }
            }
        }

        // body indent=2: top-level function body is one level deep
        let (body, params) = emit_object_body(obj, file, 2)?;
        writeln!(out, "function {}({}) {{", name, params)?;
        write!(out, "{body}")?;
        writeln!(out, "}}")?;
        writeln!(out)?;
    }

    Ok(out)
}

/* ------------------------- structuring ------------------------- */

#[derive(Clone)]
struct LoopCtx {
    header: usize,
    exit: Option<usize>,
}

#[derive(Clone, Copy)]
struct RegionOutcome {
    falls_through: bool,
}

struct Structurer<'a> {
    cfg: &'a Cfg,
    prog: &'a ExprProgram,
    fmt_var: &'a dyn Fn(VarId) -> String,

    // (pred, succ) -> list of (phi_result, incoming_value)
    edge_copies: HashMap<(usize, usize), Vec<(VarId, VarId)>>,

    // dominators / postdominators on reachable blocks
    dom: Vec<HashSet<usize>>,
    pdom: Vec<HashSet<usize>>,
    ipdom: Vec<Option<usize>>,

    // loop header -> natural loop node set
    loops: HashMap<usize, HashSet<usize>>,

    emitted: HashSet<usize>,

    // return expression per block (from SSA)
    ret_expr: Vec<Option<Expr>>,
    uses_rv: bool,
}

impl<'a> Structurer<'a> {
    fn new(
        cfg: &'a Cfg,
        prog: &'a ExprProgram,
        fmt_var: &'a dyn Fn(VarId) -> String,
        ret_expr: Vec<Option<Expr>>,
    ) -> Self {
        let edge_copies = build_edge_copies(prog);
        let reachable = compute_reachable(prog, prog.entry_block);

        let dom = compute_dominators(prog, prog.entry_block, &reachable);
        let pdom = compute_postdominators(prog, &reachable);
        let ipdom = compute_ipdom(&pdom);

        let loops = compute_natural_loops(prog, &dom, &reachable);

        let uses_rv = prog.blocks.iter().any(|b| {
            b.stmts.iter().any(|st| {
                matches!(
                    st,
                    Stmt::Opaque { op, .. }
                        if op.eq_ignore_ascii_case("SRV") || op.eq_ignore_ascii_case("VM_SRV")
                )
            })
        });

        Self {
            cfg,
            prog,
            fmt_var,
            edge_copies,
            dom,
            pdom,
            ipdom,
            loops,
            emitted: HashSet::new(),
            ret_expr,
            uses_rv,
        }
    }

    fn emit_function_body(&mut self, entry: usize, indent: usize) -> Vec<String> {
        let mut lines = Vec::new();
        let _ = self.emit_seq(entry, None, indent, None, &mut lines);
        // Unreachable blocks are silently omitted — no goto/state-machine fallback.
        simplify_empty_if_then(&mut lines);
        lines
    }

    fn emit_seq(
        &mut self,
        mut cur: usize,
        stop: Option<usize>,
        indent: usize,
        loop_ctx: Option<LoopCtx>,
        out: &mut Vec<String>,
    ) -> RegionOutcome {
        while Some(cur) != stop {
            let loop_ctx = loop_ctx.clone();
            if self.emitted.contains(&cur) {
                return RegionOutcome {
                    falls_through: true,
                };
            }

            if self.is_loop_header(cur) && stop != Some(cur) {
                let oc = self.emit_loop(cur, indent, out);
                if let Some(n) = self.loop_exit(cur) {
                    cur = n;
                    continue;
                }
                return oc;
            }

            self.emitted.insert(cur);

            self.emit_block_stmts(cur, indent, out);

            let blk = &self.prog.blocks[cur];
            match blk.term.clone() {
                Terminator::Ret => {
                    if let Some(e) = self.ret_expr.get(cur).and_then(|x| x.clone()) {
                        let s = self.expr_to_tjs(&e);
                        if s == "void" || s == "r0_0" {
                            out.push(format!("{}return;", " ".repeat(indent)));
                        } else {
                            out.push(format!("{}return {};", " ".repeat(indent), s));
                        }
                    } else {
                        out.push(format!("{}return;", " ".repeat(indent)));
                    }
                    return RegionOutcome {
                        falls_through: false,
                    };
                }
                Terminator::Throw(e) => {
                    out.push(format!(
                        "{}throw {};",
                        " ".repeat(indent),
                        self.expr_to_tjs(&e)
                    ));
                    return RegionOutcome {
                        falls_through: false,
                    };
                }
                Terminator::Exit | Terminator::Fallthrough => {
                    if let Some(n) = blk.succ.get(0).copied() {
                        self.emit_edge_copies(cur, n, indent, out);
                        cur = n;
                        continue;
                    }
                    out.push(format!("{}return;", " ".repeat(indent)));
                    return RegionOutcome {
                        falls_through: false,
                    };
                }
                Terminator::Jmp(t) => {
                    if let Some(ctx) = loop_ctx.clone() {
                        if t == ctx.header {
                            self.emit_edge_copies(cur, t, indent, out);
                            out.push(format!("{}continue;", " ".repeat(indent)));
                            return RegionOutcome {
                                falls_through: false,
                            };
                        }
                        if ctx.exit == Some(t) {
                            self.emit_edge_copies(cur, t, indent, out);
                            out.push(format!("{}break;", " ".repeat(indent)));
                            return RegionOutcome {
                                falls_through: false,
                            };
                        }
                    }
                    if stop == Some(t) {
                        self.emit_edge_copies(cur, t, indent, out);
                        return RegionOutcome {
                            falls_through: true,
                        };
                    }
                    self.emit_edge_copies(cur, t, indent, out);
                    cur = t;
                    continue;
                }
                Terminator::Br {
                    cond,
                    if_true,
                    if_false,
                } => {
                    // If this branch is a loop-exit/continue inside a loop body, prioritize break/continue patterns.
                    if let Some(ctx) = loop_ctx.clone() {
                        if if_true == ctx.header
                            || if_false == ctx.header
                            || ctx.exit == Some(if_true)
                            || ctx.exit == Some(if_false)
                        {
                            let oc = self.emit_branch_in_loop(
                                cur, &cond, if_true, if_false, indent, ctx, out,
                            );
                            return oc;
                        }
                    }

                    let join = self.ipdom.get(cur).and_then(|x| *x).or(stop);

                    // If the then-branch is trivially empty but else is not, negate and swap
                    // to avoid emitting `if (cond) { } else { ... }`.
                    let (cond_emitted, first_succ, second_succ) = if self
                        .branch_is_trivially_empty(cur, if_true, join)
                        && !self.branch_is_trivially_empty(cur, if_false, join)
                    {
                        (Expr::Unary(UnOp::Not, Box::new(cond)), if_false, if_true)
                    } else {
                        (cond, if_true, if_false)
                    };

                    out.push(format!(
                        "{}if ({}) {{",
                        " ".repeat(indent),
                        self.expr_to_tjs(&cond_emitted)
                    ));

                    // then (primary branch)
                    self.emit_edge_copies(cur, first_succ, indent + 2, out);
                    let then_oc =
                        self.emit_seq(first_succ, join, indent + 2, loop_ctx.clone(), out);
                    out.push(format!("{}}}", " ".repeat(indent)));

                    // else (secondary branch) — omit the else block when trivially empty
                    let second_is_empty = self.branch_is_trivially_empty(cur, second_succ, join);
                    let else_oc = if second_is_empty {
                        self.mark_chain_emitted(second_succ, join);
                        RegionOutcome {
                            falls_through: true,
                        }
                    } else {
                        out.push(format!("{}else {{", " ".repeat(indent)));
                        self.emit_edge_copies(cur, second_succ, indent + 2, out);
                        let oc = self.emit_seq(second_succ, join, indent + 2, loop_ctx, out);
                        out.push(format!("{}}}", " ".repeat(indent)));
                        oc
                    };

                    if let Some(j) = join {
                        if then_oc.falls_through || else_oc.falls_through {
                            cur = j;
                            continue;
                        }
                        return RegionOutcome {
                            falls_through: false,
                        };
                    }
                    return RegionOutcome {
                        falls_through: then_oc.falls_through || else_oc.falls_through,
                    };
                }
            }
        }

        RegionOutcome {
            falls_through: true,
        }
    }

    fn emit_branch_in_loop(
        &mut self,
        cur: usize,
        cond: &Expr,
        t: usize,
        f: usize,
        indent: usize,
        ctx: LoopCtx,
        out: &mut Vec<String>,
    ) -> RegionOutcome {
        // Pattern:
        // if (cond) { ... } else { ... }
        // but allow branches to be break/continue.
        out.push(format!(
            "{}if ({}) {{",
            " ".repeat(indent),
            self.expr_to_tjs(cond)
        ));

        self.emit_edge_copies(cur, t, indent + 2, out);
        let then_oc = self.emit_seq(t, None, indent + 2, Some(ctx.clone()), out);
        out.push(format!("{}}}", " ".repeat(indent)));

        out.push(format!("{}else {{", " ".repeat(indent)));
        self.emit_edge_copies(cur, f, indent + 2, out);
        let else_oc = self.emit_seq(f, None, indent + 2, Some(ctx), out);
        out.push(format!("{}}}", " ".repeat(indent)));

        RegionOutcome {
            falls_through: then_oc.falls_through || else_oc.falls_through,
        }
    }

    fn is_loop_header(&self, h: usize) -> bool {
        self.loops.contains_key(&h)
    }

    fn loop_exit(&self, h: usize) -> Option<usize> {
        let body = self.loops.get(&h)?;
        let blk = &self.prog.blocks[h];
        for &s in &blk.succ {
            if !body.contains(&s) {
                return Some(s);
            }
        }
        None
    }

    fn emit_loop(&mut self, header: usize, indent: usize, out: &mut Vec<String>) -> RegionOutcome {
        let body_nodes = match self.loops.get(&header) {
            Some(s) => s.clone(),
            None => {
                return RegionOutcome {
                    falls_through: true,
                };
            }
        };

        // Choose loop exit as header successor not in loop set.
        let exit = self.loop_exit(header);

        out.push(format!("{}while (true) {{", " ".repeat(indent)));

        // Emit header statements inside loop.
        self.emit_block_stmts(header, indent + 2, out);

        // Handle header terminator as loop guard / dispatch.
        let blk = &self.prog.blocks[header];
        match blk.term.clone() {
            Terminator::Br {
                cond,
                if_true,
                if_false,
            } => {
                // Decide which successor stays in loop.
                let t_in = body_nodes.contains(&if_true);
                let f_in = body_nodes.contains(&if_false);

                if exit.is_some() && (t_in ^ f_in) {
                    let (body_succ, exit_succ, break_on_true) = if t_in {
                        (if_true, if_false, false)
                    } else {
                        (if_false, if_true, true)
                    };

                    if break_on_true {
                        // if (cond) { copies; break; }
                        out.push(format!(
                            "{}if ({}) {{",
                            " ".repeat(indent + 2),
                            self.expr_to_tjs(&cond)
                        ));
                        self.emit_edge_copies(header, exit_succ, indent + 4, out);
                        out.push(format!("{}break;", " ".repeat(indent + 4)));
                        out.push(format!("{}}}", " ".repeat(indent + 2)));
                    } else {
                        // if (!cond) { copies; break; }
                        let ncond = Expr::Unary(UnOp::Not, Box::new(cond));
                        out.push(format!(
                            "{}if ({}) {{",
                            " ".repeat(indent + 2),
                            self.expr_to_tjs(&ncond)
                        ));
                        self.emit_edge_copies(header, exit_succ, indent + 4, out);
                        out.push(format!("{}break;", " ".repeat(indent + 4)));
                        out.push(format!("{}}}", " ".repeat(indent + 2)));
                    }

                    // fall into body
                    self.emit_edge_copies(header, body_succ, indent + 2, out);
                    let _ = self.emit_seq(
                        body_succ,
                        Some(header),
                        indent + 2,
                        Some(LoopCtx { header, exit }),
                        out,
                    );
                } else {
                    // Fallback: still emit both arms inside loop (no goto/state machine).
                    out.push(format!(
                        "{}if ({}) {{",
                        " ".repeat(indent + 2),
                        self.expr_to_tjs(&cond)
                    ));
                    self.emit_edge_copies(header, if_true, indent + 4, out);
                    let _ = self.emit_seq(
                        if_true,
                        Some(header),
                        indent + 4,
                        Some(LoopCtx { header, exit }),
                        out,
                    );
                    out.push(format!("{}}}", " ".repeat(indent + 2)));
                    out.push(format!("{}else {{", " ".repeat(indent + 2)));
                    self.emit_edge_copies(header, if_false, indent + 4, out);
                    let _ = self.emit_seq(
                        if_false,
                        Some(header),
                        indent + 4,
                        Some(LoopCtx { header, exit }),
                        out,
                    );
                    out.push(format!("{}}}", " ".repeat(indent + 2)));
                }
            }
            Terminator::Jmp(t) => {
                if t == header {
                    out.push(format!("{}continue;", " ".repeat(indent + 2)));
                } else {
                    self.emit_edge_copies(header, t, indent + 2, out);
                    let _ = self.emit_seq(
                        t,
                        Some(header),
                        indent + 2,
                        Some(LoopCtx { header, exit }),
                        out,
                    );
                }
            }
            Terminator::Ret => {
                if let Some(e) = self.ret_expr.get(header).and_then(|x| x.clone()) {
                    let s = self.expr_to_tjs(&e);
                    if s == "void" || s == "r0_0" {
                        out.push(format!("{}return;", " ".repeat(indent + 2)));
                    } else {
                        out.push(format!("{}return {};", " ".repeat(indent + 2), s));
                    }
                } else {
                    out.push(format!("{}return;", " ".repeat(indent + 2)));
                }
            }
            Terminator::Throw(e) => {
                out.push(format!(
                    "{}throw {};",
                    " ".repeat(indent + 2),
                    self.expr_to_tjs(&e)
                ));
            }
            Terminator::Exit | Terminator::Fallthrough => {
                if let Some(n) = blk.succ.get(0).copied() {
                    self.emit_edge_copies(header, n, indent + 2, out);
                    let _ = self.emit_seq(
                        n,
                        Some(header),
                        indent + 2,
                        Some(LoopCtx { header, exit }),
                        out,
                    );
                } else {
                    out.push(format!("{}return;", " ".repeat(indent + 2)));
                }
            }
        }

        out.push(format!("{}}}", " ".repeat(indent)));

        // Mark all nodes in this loop as emitted (except those already).
        for n in body_nodes {
            self.emitted.insert(n);
        }
        self.emitted.insert(header);

        RegionOutcome {
            falls_through: exit.is_some(),
        }
    }

    /// Returns true when branching from `pred` to `succ` (with `stop` as the region limit)
    /// would emit zero lines: no non-trivial edge copies, no block statements, and every block
    /// in the single-successor chain eventually falls to `stop` (follows Jmp/Fallthrough/Exit
    /// only, up to `depth` hops, with cycle detection).
    fn branch_is_trivially_empty(&self, pred: usize, succ: usize, stop: Option<usize>) -> bool {
        let mut visited = HashSet::new();
        self.chain_is_empty(pred, succ, stop, &mut visited, 16)
    }

    fn chain_is_empty(
        &self,
        pred: usize,
        succ: usize,
        stop: Option<usize>,
        visited: &mut HashSet<usize>,
        depth: usize,
    ) -> bool {
        // Always check edge copies from pred→succ first (including when succ==stop),
        // so that live phi edge copies on the final hop are not silently skipped.
        if let Some(xs) = self.edge_copies.get(&(pred, succ)) {
            for (d, s) in xs {
                if (self.fmt_var)(*d) != (self.fmt_var)(*s) {
                    return false;
                }
            }
        }
        if Some(succ) == stop {
            return true;
        }
        if depth == 0 || !visited.insert(succ) {
            return false;
        }
        let blk = &self.prog.blocks[succ];
        // Any non-control stmt → not empty.
        for st in &blk.stmts {
            if !matches!(st, Stmt::Opaque { op, .. } if is_control_op(op)) {
                return false;
            }
        }
        // Follow single-successor terminators only.
        match &blk.term {
            Terminator::Jmp(t) => self.chain_is_empty(succ, *t, stop, visited, depth - 1),
            Terminator::Fallthrough | Terminator::Exit => match blk.succ.get(0).copied() {
                Some(t) => self.chain_is_empty(succ, t, stop, visited, depth - 1),
                None => stop.is_none(),
            },
            _ => false,
        }
    }

    /// Mark all blocks in the single-successor chain from `succ` up to (but not including)
    /// `stop` as emitted.  Called when we skip an empty branch entirely.
    fn mark_chain_emitted(&mut self, succ: usize, stop: Option<usize>) {
        let mut cur = succ;
        loop {
            if Some(cur) == stop || !self.emitted.insert(cur) {
                break;
            }
            let blk = &self.prog.blocks[cur];
            match &blk.term {
                Terminator::Jmp(t) => cur = *t,
                Terminator::Fallthrough | Terminator::Exit => match blk.succ.get(0).copied() {
                    Some(t) => cur = t,
                    None => break,
                },
                _ => break,
            }
        }
    }

    fn emit_block_stmts(&self, bid: usize, indent: usize, out: &mut Vec<String>) {
        let blk = &self.prog.blocks[bid];
        for st in &blk.stmts {
            if let Stmt::Opaque { op, .. } = st {
                if is_control_op(op) {
                    continue;
                }
            }
            let s = self.stmt_to_tjs(st);
            if s.is_empty() || s == "// (control op omitted)" {
                continue;
            }
            out.push(format!("{}{}", " ".repeat(indent), s));
        }
    }

    fn emit_edge_copies(&self, pred: usize, succ: usize, indent: usize, out: &mut Vec<String>) {
        if let Some(xs) = self.edge_copies.get(&(pred, succ)) {
            for (dst, src) in xs {
                let d = (self.fmt_var)(*dst);
                // r0_0 (initial void of result register) renders as "void".
                let s = if src.var == Var::Reg(0) && src.ver == 0 {
                    "void".to_string()
                } else {
                    (self.fmt_var)(*src)
                };
                if d == s {
                    continue; // skip self-assignments
                }
                out.push(format!("{}{} = {};", " ".repeat(indent), d, s));
            }
        }
    }

    fn stmt_to_tjs(&self, st: &Stmt) -> String {
        match st {
            Stmt::Assign { dst, expr } => {
                format!("{} = {};", (self.fmt_var)(*dst), self.expr_to_tjs(expr))
            }
            Stmt::Store { target, value } => {
                format!(
                    "{} = {};",
                    self.expr_to_tjs(target),
                    self.expr_to_tjs(value)
                )
            }
            Stmt::Update {
                dst,
                target,
                op,
                rhs,
            } => {
                if let Some(comp) = to_compound_assign(*op) {
                    if let Some(d) = dst {
                        format!(
                            "{} = ({} {} {});",
                            (self.fmt_var)(*d),
                            self.expr_to_tjs(target),
                            comp.op_str(),
                            self.expr_to_tjs(rhs)
                        )
                    } else {
                        format!(
                            "{} {} {};",
                            self.expr_to_tjs(target),
                            comp.op_str(),
                            self.expr_to_tjs(rhs)
                        )
                    }
                } else {
                    if let Some(d) = dst {
                        format!(
                            "{} = ({} = ({} {} {}));",
                            (self.fmt_var)(*d),
                            self.expr_to_tjs(target),
                            self.expr_to_tjs(target),
                            op.op_str(),
                            self.expr_to_tjs(rhs)
                        )
                    } else {
                        format!(
                            "{} = ({} {} {});",
                            self.expr_to_tjs(target),
                            self.expr_to_tjs(target),
                            op.op_str(),
                            self.expr_to_tjs(rhs)
                        )
                    }
                }
            }
            Stmt::Expr(e) => format!("{};", self.expr_to_tjs(e)),
            Stmt::Opaque { op, args, defs } => {
                match op.to_string().as_str() {
                    "JF" | "JNF" | "JMP" | "RET" | "THROW" | "ENTRY" | "EXTRY" | "VM_JF"
                    | "VM_JNF" | "VM_JMP" | "VM_RET" | "VM_THROW" | "VM_ENTRY" | "VM_EXTRY" => {
                        return "// (control op omitted)".to_string();
                    }
                    _ => {}
                }
                let op_name = op.to_string();
                if op_name == "VM_CHGTHIS" || op_name == "CHGTHIS" {
                    return "// (this-change op omitted)".to_string();
                }

                if (op_name == "VM_TYPEOFD"
                    || op_name == "TYPEOFD"
                    || op_name == "VM_TYPEOF"
                    || op_name == "TYPEOF")
                    && args.len() == 1
                {
                    let x = args[0].to_tjs_with(self.fmt_var);
                    let expr = format!("(typeof {})", x);

                    if defs.is_empty() {
                        return format!("{};", expr);
                    } else if defs.len() == 1 {
                        return format!("{} = {};", (self.fmt_var)(defs[0]), expr);
                    } else {
                        let mut s = String::new();
                        let _ = write!(&mut s, "{{ var __t = {}; ", expr);
                        for (i, d) in defs.iter().enumerate() {
                            let _ = write!(&mut s, "{} = __t[{}]; ", (self.fmt_var)(*d), i);
                        }
                        let _ = write!(&mut s, "}}");
                        return s;
                    }
                }

                if op_name == "VM_SRV" || op_name == "SRV" {
                    // SRV is represented by ret_expr in the Structurer; suppress inline output.
                    return String::new();
                }

                if (op_name == "VM_NUM" || op_name == "NUM") && args.len() == 1 {
                    let x = args[0].to_tjs_with(self.fmt_var);

                    let expr = format!("real({})", x);

                    if defs.len() == 1 {
                        return format!("{} = {};", (self.fmt_var)(defs[0]), expr);
                    } else {
                        return format!("{};", expr);
                    }
                }

                if (op_name.starts_with("VM_STR") || op_name == "STR") && args.len() == 1 {
                    let x = args[0].to_tjs_with(self.fmt_var);
                    let expr = format!("string({})", x);

                    if defs.len() == 1 {
                        return format!("{} = {};", (self.fmt_var)(defs[0]), expr);
                    } else {
                        return format!("{};", expr);
                    }
                }

                if op_name == "VM_CHGTHIS" || op_name == "CHGTHIS" {
                    if args.len() == 2 {
                        return format!(
                            "chgthis({}, {});",
                            args[0].to_tjs_with(self.fmt_var),
                            args[1].to_tjs_with(self.fmt_var),
                        );
                    }
                    return "// chgthis();".to_string();
                }

                if op_name.starts_with("VM_REGMEMBER") && args.len() == 3 {
                    return format!(
                        "{}.{} = {};",
                        args[0].to_tjs_with(self.fmt_var),
                        args[1].to_tjs_with(self.fmt_var),
                        args[2].to_tjs_with(self.fmt_var)
                    );
                }

                if op_name.starts_with("VM_INV") && args.len() >= 2 {
                    let recv = args[0].to_tjs_with(self.fmt_var);
                    let method = args[1].to_tjs_with(self.fmt_var);
                    let call_args = args
                        .iter()
                        .skip(2)
                        .map(|x| x.to_tjs_with(self.fmt_var))
                        .collect::<Vec<_>>()
                        .join(", ");
                    let call = format!("{}.{}({})", recv, method, call_args);
                    if defs.len() == 1 {
                        return format!("{} = {};", (self.fmt_var)(defs[0]), call);
                    } else {
                        return format!("{};", call);
                    }
                }

                let call = if args.is_empty() {
                    format!("{}()", op)
                } else {
                    // let mut s = String::new();
                    // s.push_str(op);
                    // s.push('(');
                    // for (i, a) in args.iter().enumerate() {
                    //     if i != 0 {
                    //         s.push_str(", ");
                    //     }
                    //     s.push_str(&self.expr_to_tjs(a));
                    // }
                    // s.push(')');

                    let a0 = args.get(0).map(|x| x.to_tjs_with(self.fmt_var));
                    let a1 = args.get(1).map(|x| x.to_tjs_with(self.fmt_var));

                    let opname = op;

                    let call = if let (Some(x), Some(y)) = (a0.as_deref(), a1.as_deref()) {
                        // binary families (cover D/I/P variants by starts_with)
                        if opname.starts_with("VM_ADD") {
                            format!("({} + {})", x, y)
                        } else if opname.starts_with("VM_SUB") {
                            format!("({} - {})", x, y)
                        } else if opname.starts_with("VM_MUL") {
                            format!("({} * {})", x, y)
                        } else if opname.starts_with("VM_DIV") {
                            format!("({} / {})", x, y)
                        } else if opname.starts_with("VM_IDIV") {
                            format!("({} \\ {})", x, y)
                        } else if opname.starts_with("VM_MOD") {
                            format!("({} % {})", x, y)
                        } else if opname.starts_with("VM_SAL") {
                            format!("({} << {})", x, y)
                        } else if opname.starts_with("VM_SAR") {
                            format!("({} >> {})", x, y)
                        } else if opname.starts_with("VM_SR") {
                            format!("({} >>> {})", x, y)
                        } else if opname.starts_with("VM_BAND") {
                            format!("({} & {})", x, y)
                        } else if opname.starts_with("VM_BXOR") {
                            format!("({} ^ {})", x, y)
                        } else if opname.starts_with("VM_BOR") {
                            format!("({} | {})", x, y)
                        } else if opname.starts_with("VM_LAND") {
                            format!("({} && {})", x, y)
                        } else if opname.starts_with("VM_LOR") {
                            format!("({} || {})", x, y)
                        } else if opname.starts_with("VM_EQ") {
                            format!("({} == {})", x, y)
                        } else if opname.starts_with("VM_NE") {
                            format!("({} != {})", x, y)
                        } else if opname.starts_with("VM_DEQ") {
                            format!("({} === {})", x, y)
                        } else if opname.starts_with("VM_DNE") {
                            format!("({} !== {})", x, y)
                        } else if opname.starts_with("VM_LT") {
                            format!("({} < {})", x, y)
                        } else if opname.starts_with("VM_LE") {
                            format!("({} <= {})", x, y)
                        } else if opname.starts_with("VM_GT") {
                            format!("({} > {})", x, y)
                        } else if opname.starts_with("VM_GE") {
                            format!("({} >= {})", x, y)
                        } else if opname.to_string() == "CHKINS" || opname.starts_with("VM_IN") {
                            format!("({} in {})", x, y)
                        } else {
                            // fallback to original call form
                            let mut s = String::new();
                            s.push_str(op);
                            s.push('(');
                            for (i, a) in args.iter().enumerate() {
                                if i != 0 {
                                    s.push_str(", ");
                                }
                                s.push_str(&a.to_tjs_with(self.fmt_var));
                            }
                            s.push(')');
                            s
                        }
                    } else if let Some(x) = a0.as_deref() {
                        // unary families (also cover variants)
                        if opname.starts_with("VM_CHS") {
                            format!("(-{})", x)
                        } else if opname.starts_with("VM_LNOT") {
                            format!("(!{})", x)
                        } else if opname.starts_with("VM_BNOT") {
                            format!("(~{})", x)
                        } else if opname.starts_with("VM_TYPEOF") {
                            format!("(typeof {})", x)
                        } else if opname.starts_with("VM_DELETE") {
                            format!("(delete {})", x)
                        } else if opname.starts_with("VM_INC") {
                            format!("({} + 1)", x)
                        } else if opname.starts_with("VM_DEC") {
                            format!("({} - 1)", x)
                        } else {
                            // fallback
                            let mut s = String::new();
                            s.push_str(op);
                            s.push('(');
                            for (i, a) in args.iter().enumerate() {
                                if i != 0 {
                                    s.push_str(", ");
                                }
                                s.push_str(&a.to_tjs_with(self.fmt_var));
                            }
                            s.push(')');
                            s
                        }
                    } else {
                        format!("{}()", op)
                    };

                    call
                };

                if defs.is_empty() {
                    format!("{};", call)
                } else if defs.len() == 1 {
                    format!("{} = {};", (self.fmt_var)(defs[0]), call)
                } else {
                    // Multiple defs: use a temp array-like value.
                    // Still no helper functions; just structured, explicit assignments.
                    let mut s = String::new();
                    s.push_str("{ ");
                    s.push_str("var __t = ");
                    s.push_str(&call);
                    s.push_str("; ");
                    for (i, d) in defs.iter().enumerate() {
                        let _ = write!(&mut s, "{} = __t[{}]; ", (self.fmt_var)(*d), i);
                    }
                    s.push_str("}");
                    s
                }
            }
        }
    }

    fn expr_to_tjs(&self, e: &Expr) -> String {
        e.to_tjs_with(self.fmt_var)
    }
}

/* ------------------------- utilities ------------------------- */

fn build_edge_copies(prog: &ExprProgram) -> HashMap<(usize, usize), Vec<(VarId, VarId)>> {
    let mut m: HashMap<(usize, usize), Vec<(VarId, VarId)>> = HashMap::new();
    for b in &prog.blocks {
        for phi in &b.phi {
            for (pred, v) in &phi.args {
                m.entry((*pred, b.id)).or_default().push((phi.result, *v));
            }
        }
    }
    m
}

fn compute_reachable(prog: &ExprProgram, entry: usize) -> HashSet<usize> {
    let mut seen = HashSet::new();
    let mut stack = vec![entry];
    while let Some(n) = stack.pop() {
        if !seen.insert(n) {
            continue;
        }
        for &s in &prog.blocks[n].succ {
            stack.push(s);
        }
    }
    seen
}

fn compute_dominators(
    prog: &ExprProgram,
    entry: usize,
    reachable: &HashSet<usize>,
) -> Vec<HashSet<usize>> {
    let n = prog.blocks.len();
    let all: HashSet<usize> = (0..n).filter(|x| reachable.contains(x)).collect();

    let mut dom = vec![HashSet::new(); n];
    for b in 0..n {
        if !reachable.contains(&b) {
            continue;
        }
        if b == entry {
            dom[b].insert(entry);
        } else {
            dom[b] = all.clone();
        }
    }

    let mut changed = true;
    while changed {
        changed = false;
        for b in 0..n {
            if !reachable.contains(&b) || b == entry {
                continue;
            }
            let preds = &prog.blocks[b].pred;
            if preds.is_empty() {
                continue;
            }
            let mut nd = all.clone();
            for &p in preds {
                if !reachable.contains(&p) {
                    continue;
                }
                nd = nd
                    .intersection(&dom[p])
                    .copied()
                    .collect::<HashSet<usize>>();
            }
            nd.insert(b);
            if nd != dom[b] {
                dom[b] = nd;
                changed = true;
            }
        }
    }
    dom
}

fn compute_postdominators(prog: &ExprProgram, reachable: &HashSet<usize>) -> Vec<HashSet<usize>> {
    let n = prog.blocks.len();
    let all: HashSet<usize> = (0..n).filter(|x| reachable.contains(x)).collect();

    let exits: HashSet<usize> = (0..n)
        .filter(|b| {
            if !reachable.contains(b) {
                return false;
            }
            matches!(
                prog.blocks[*b].term,
                Terminator::Ret | Terminator::Throw(_) // Exit/Fallthrough with no succ also treated later
            ) || prog.blocks[*b].succ.is_empty()
        })
        .collect();

    let mut pdom = vec![HashSet::new(); n];
    for b in 0..n {
        if !reachable.contains(&b) {
            continue;
        }
        if exits.contains(&b) {
            pdom[b].insert(b);
        } else {
            pdom[b] = all.clone();
        }
    }

    let mut changed = true;
    while changed {
        changed = false;
        for b in 0..n {
            if !reachable.contains(&b) || exits.contains(&b) {
                continue;
            }
            let succs = &prog.blocks[b].succ;
            if succs.is_empty() {
                continue;
            }
            let mut nd = all.clone();
            for &s in succs {
                if !reachable.contains(&s) {
                    continue;
                }
                nd = nd
                    .intersection(&pdom[s])
                    .copied()
                    .collect::<HashSet<usize>>();
            }
            nd.insert(b);
            if nd != pdom[b] {
                pdom[b] = nd;
                changed = true;
            }
        }
    }
    pdom
}

fn compute_ipdom(pdom: &[HashSet<usize>]) -> Vec<Option<usize>> {
    let n = pdom.len();
    let mut ip = vec![None; n];
    for b in 0..n {
        let mut cand: Vec<usize> = pdom[b].iter().copied().collect();
        cand.retain(|x| *x != b);
        if cand.is_empty() {
            continue;
        }
        // pick c such that no other candidate post-dominates c
        let mut picked = None;
        'outer: for &c in &cand {
            for &d in &cand {
                if d == c {
                    continue;
                }
                if pdom[d].contains(&c) {
                    continue 'outer;
                }
            }
            picked = Some(c);
            break;
        }
        ip[b] = picked;
    }
    ip
}

fn compute_natural_loops(
    prog: &ExprProgram,
    dom: &[HashSet<usize>],
    reachable: &HashSet<usize>,
) -> HashMap<usize, HashSet<usize>> {
    let mut loops: HashMap<usize, HashSet<usize>> = HashMap::new();
    for u in 0..prog.blocks.len() {
        if !reachable.contains(&u) {
            continue;
        }
        for &v in &prog.blocks[u].succ {
            if !reachable.contains(&v) {
                continue;
            }
            // back edge u -> v if v dominates u
            if dom[u].contains(&v) {
                let mut set = HashSet::new();
                set.insert(v);
                set.insert(u);
                let mut stack = vec![u];
                while let Some(x) = stack.pop() {
                    for &p in &prog.blocks[x].pred {
                        if !reachable.contains(&p) {
                            continue;
                        }
                        if set.insert(p) {
                            stack.push(p);
                        }
                    }
                }
                loops
                    .entry(v)
                    .and_modify(|s| {
                        for n in &set {
                            s.insert(*n);
                        }
                    })
                    .or_insert(set);
            }
        }
    }
    loops
}

fn to_compound_assign(op: BinOp) -> Option<BinOp> {
    Some(match op {
        BinOp::Add => BinOp::AddAssign,
        BinOp::Sub => BinOp::SubAssign,
        BinOp::Mul => BinOp::MulAssign,
        BinOp::Div => BinOp::DivAssign,
        BinOp::Mod => BinOp::ModAssign,
        BinOp::Shl => BinOp::ShlAssign,
        BinOp::Shr => BinOp::ShrAssign,
        BinOp::UShr => BinOp::UShrAssign,
        BinOp::BitAnd => BinOp::AndAssign,
        BinOp::BitOr => BinOp::OrAssign,
        BinOp::BitXor => BinOp::XorAssign,
        _ => return None,
    })
}

fn is_control_op(op: &str) -> bool {
    let bare = op.strip_prefix("VM_").unwrap_or(op);
    bare.eq_ignore_ascii_case("JMP")
        || bare.eq_ignore_ascii_case("JF")
        || bare.eq_ignore_ascii_case("JNF")
        || bare.eq_ignore_ascii_case("RET")
        || bare.eq_ignore_ascii_case("THROW")
        || bare.eq_ignore_ascii_case("ENTRY")
        || bare.eq_ignore_ascii_case("EXTRY")
}

fn emit_var_decls(
    out: &mut String,
    prog: &ExprProgram,
    fmt_var: &dyn Fn(VarId) -> String,
    arg_count: usize,
    indent: usize,
) -> Result<()> {
    let mut vars: Vec<VarId> = collect_vars(prog);
    vars.sort_by_key(|v| (var_key(v), v.ver));
    // Declare positive registers, frame locals (_fr*), and special vars.
    // Do NOT declare declared params (a0..a{n-1}) or special regs (-1=this, -2=global/this).
    // Also skip r0_0 (ver=0 of reg 0) — it's always void and never declared.
    vars.retain(|v| match v.var {
        Var::Reg(r) if r >= 0 => !(r == 0 && v.ver == 0), // skip r0_0
        Var::Reg(r) if r <= -3 => (-3 - r) as usize >= arg_count, // frame locals only, not args
        Var::Flag | Var::Exception => true,
        _ => false,
    });
    vars.dedup_by_key(|v| fmt_var(*v));
    if vars.is_empty() {
        return Ok(());
    }

    let pad = " ".repeat(indent);
    let mut i = 0usize;
    while i < vars.len() {
        let end = (i + 12).min(vars.len());
        write!(out, "{}var ", pad)?;
        for j in i..end {
            if j != i {
                write!(out, ", ")?;
            }
            write!(out, "{}", fmt_var(vars[j]))?;
        }
        writeln!(out, ";")?;
        i = end;
    }
    Ok(())
}

fn collect_vars(prog: &ExprProgram) -> Vec<VarId> {
    let mut s: HashSet<VarId> = HashSet::new();

    for b in &prog.blocks {
        for p in &b.phi {
            s.insert(p.result);
            for (_pred, v) in &p.args {
                s.insert(*v);
            }
        }
        for st in &b.stmts {
            collect_vars_stmt(st, &mut s);
        }
        collect_vars_term(&b.term, &mut s);
    }

    s.into_iter().collect()
}

fn collect_vars_stmt(st: &Stmt, s: &mut HashSet<VarId>) {
    match st {
        Stmt::Assign { dst, expr } => {
            s.insert(*dst);
            collect_vars_expr(expr, s);
        }
        Stmt::Store { target, value } => {
            collect_vars_expr(target, s);
            collect_vars_expr(value, s);
        }
        Stmt::Update {
            dst, target, rhs, ..
        } => {
            if let Some(d) = dst {
                s.insert(*d);
            }
            collect_vars_expr(target, s);
            collect_vars_expr(rhs, s);
        }
        Stmt::Expr(e) => collect_vars_expr(e, s),
        Stmt::Opaque { args, defs, .. } => {
            for d in defs {
                s.insert(*d);
            }
            for a in args {
                collect_vars_expr(a, s);
            }
        }
    }
}

fn collect_vars_term(t: &Terminator, s: &mut HashSet<VarId>) {
    match t {
        Terminator::Br { cond, .. } => collect_vars_expr(cond, s),
        Terminator::Throw(e) => collect_vars_expr(e, s),
        _ => {}
    }
}

fn collect_vars_expr(e: &Expr, s: &mut HashSet<VarId>) {
    match e {
        Expr::SsaVar(v) => {
            s.insert(*v);
        }
        Expr::Unary(_, a) => collect_vars_expr(a, s),
        Expr::Deref(a) => collect_vars_expr(a, s),
        Expr::Binary(_, a, b) => {
            collect_vars_expr(a, s);
            collect_vars_expr(b, s);
        }
        Expr::Call(f, args) | Expr::New(f, args) => {
            collect_vars_expr(f, s);
            for a in args {
                collect_vars_expr(a, s);
            }
        }
        Expr::Index(a, b) => {
            collect_vars_expr(a, s);
            collect_vars_expr(b, s);
        }
        Expr::Member(a, _) => collect_vars_expr(a, s),
        Expr::MethodCall { base, args, .. } => {
            collect_vars_expr(base, s);
            for a in args {
                collect_vars_expr(a, s);
            }
        }
        Expr::Opaque(_, args) => {
            for a in args {
                collect_vars_expr(a, s);
            }
        }
        _ => {}
    }
}

fn var_key(v: &VarId) -> (u8, i32) {
    match v.var {
        Var::Reg(r) => (0, r),
        Var::Flag => (1, 0),
        Var::Exception => (2, 0),
    }
}

fn fmt_vid_tjs(vid: VarId) -> String {
    match vid.var {
        Var::Reg(r) if r >= 0 => format!("r{}_{}", r, vid.ver),
        Var::Reg(-1) => "this".to_string(),
        Var::Reg(-2) => "global".to_string(),
        Var::Reg(r) => format!("a{}", (-3 - r) as usize),
        Var::Flag => format!("flag_{}", vid.ver),
        Var::Exception => format!("exc_{}", vid.ver),
    }
}

fn obj_lhs(index: usize, name: Option<&str>) -> String {
    if let Some(n) = name {
        let parts: Vec<&str> = n.split('.').collect();
        if !parts.is_empty() && parts.iter().all(|p| is_identifier(p)) {
            return parts.join(".");
        }
    }
    format!("obj{}", index)
}

/// Post-processing pass: collapse `if (cond) { } else { ... }` into `if (!cond) { ... }`.
/// Operates on a flat list of lines with consistent indentation.
fn simplify_empty_if_then(lines: &mut Vec<String>) {
    let mut i = 0;
    while i + 2 < lines.len() {
        let ind0 = leading_spaces(&lines[i]);
        let ind1 = leading_spaces(&lines[i + 1]);
        let ind2 = leading_spaces(&lines[i + 2]);
        let ln0 = lines[i][ind0..].trim_end();
        let ln1 = lines[i + 1][ind1..].trim_end();
        let ln2 = lines[i + 2][ind2..].trim_end();

        if ind0 == ind1
            && ind0 == ind2
            && ln0.starts_with("if (")
            && ln0.ends_with(") {")
            && ln1 == "}"
            && ln2 == "else {"
        {
            let cond = &ln0["if (".len()..ln0.len() - ") {".len()];
            let ncond = negate_str_cond(cond);
            let spaces = " ".repeat(ind0);
            lines[i] = format!("{}if ({}) {{", spaces, ncond);
            lines.remove(i + 2); // "else {"
            lines.remove(i + 1); // "}"
        // Don't increment — recheck this line in case of further nesting.
        } else {
            i += 1;
        }
    }
}

fn leading_spaces(s: &str) -> usize {
    s.len() - s.trim_start().len()
}

/// Negate a condition string syntactically:
/// - `"!expr"` / `"!(inner)"` → strip outer negation
/// - simple identifier → `"!ident"`
/// - anything else → `"!(cond)"`
fn negate_str_cond(cond: &str) -> String {
    if let Some(rest) = cond.strip_prefix('!') {
        if rest.starts_with('(') && rest.ends_with(')') {
            rest[1..rest.len() - 1].to_string()
        } else {
            rest.to_string()
        }
    } else if cond.chars().all(|c| c.is_alphanumeric() || c == '_') {
        format!("!{}", cond)
    } else {
        format!("!({})", cond)
    }
}

fn is_identifier(s: &str) -> bool {
    let mut it = s.chars();
    let Some(c0) = it.next() else {
        return false;
    };
    if !(c0 == '_' || c0.is_ascii_alphabetic()) {
        return false;
    }
    it.all(|c| c == '_' || c.is_ascii_alphanumeric())
}
