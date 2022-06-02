class HashTable:
    def __init__(self, table_size):
        self.size = table_size    # 총 공간(bucket) 수
        self.hash_table = [0 for a in range(self.size)]    # 빈 hash table 생성

    def getKey(self, data):    # key(문자) 첫 문자의 유니코드를 반환
        self.key = ord(data[0])
        return self.key

    def hashFunction(self, key):    # key 의 hash 값을 반환
        return key % self.size

    def getAddress(self, key):    # hash address 를 반환
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    def save(self, key, value):    # 데이터 저장
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value

    def read(self, key):    # key 에 해당하는 value 반환
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]

    def delete(self, key):    # 데이터 삭제
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        else:
            return False


if __name__ == '__main__':
    h_table = HashTable(8)
    h_table.save('a', '1111')
    h_table.save('b', '2222')
    h_table.save('c', '3333')
    h_table.save('d', '4444')

    print(h_table.hash_table)  # [0, '1111', '2222', '3333', '4444', 0, 0, 0]

    print(h_table.read('d'))  # 4444

    h_table.delete('d')

    print(h_table.hash_table)  # [0, '1111', '2222', 0, '4444', 0, 0, 0]
