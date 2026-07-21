#ifndef MAITETSU_DEC_HPP
#define MAITETSU_DEC_HPP

#include <cstdint>
#include <vector>
#include <cstddef>

class MaitetsuCxDecryption {
public:
    MaitetsuCxDecryption();
    ~MaitetsuCxDecryption() = default;

    // Decrypt in-place buffer using Maitetsu CxEncryption algorithm
    void decrypt_buffer(uint32_t hash_val, size_t offset, uint8_t* buffer, size_t count);

private:
    void init_seed_tables();
};

#endif // MAITETSU_DEC_HPP
