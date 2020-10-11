from math import sqrt, pow, pi
import random


HASH_TABLE_LENGTH = 55
KEYS_NUM = 50
MAX_KEY_VALUE = 25
NUM_KEYS_PORTIONS = 5
HASH_CONSTANT_LIST = [(sqrt(5) - 1)/2, pow(2, 32) * 2/(sqrt(5) - 1), sqrt(18*pi)/5, pi, 5*sqrt(pi/20), (19*sqrt(33) - 47) / 17]
VALUE_IN_HASH_TABLE_TEMPLATE = 'value number '


def initialize_hashtable(hash_table_length) -> list:
    return [None for _ in range(hash_table_length)]


def initialize_hashtable_with_chains(hash_table_length) -> list:
    return [[] for _ in range(hash_table_length)]


def hash_multiplication_method(key, hash_table_length, MULTIPLICATION_CONST):
    return int(hash_table_length * (key * MULTIPLICATION_CONST - int(key * MULTIPLICATION_CONST)))


def insert_into_hash_table_with_chains(hash_table, key, value, HASH_MULTIPLICATION_CONSTANT):
    hash_key = hash_multiplication_method(key, HASH_TABLE_LENGTH, HASH_MULTIPLICATION_CONSTANT)
    hash_table[hash_key].append(value)


def insert_into_hash_table_with_linear_probing(hash_table, key, value, HASH_MULTIPLICATION_CONSTANT):
    hash_key = hash_multiplication_method(key, HASH_TABLE_LENGTH, HASH_MULTIPLICATION_CONSTANT)

    for i in range(HASH_TABLE_LENGTH):
        if not hash_table[(hash_key + i) % len(hash_table)]:
            hash_table[(hash_key + i) % len(hash_table)] = value
            break


def insert_into_hash_table_with_double_hashing(hash_table, key, value, MULTIPLICATION_CONST_1, MULTIPLICATION_CONST_2):
    hash_of_1_const = hash_multiplication_method(key, len(hash_table), MULTIPLICATION_CONST_1)
    hash_of_2_const = hash_multiplication_method(key, len(hash_table), MULTIPLICATION_CONST_2)
    for i in range(len(hash_table)):
        if not hash_table[(hash_of_1_const + i*hash_of_2_const) % len(hash_table)]:
            hash_table[(hash_of_1_const + i * hash_of_2_const) % len(hash_table)] = value
            break


def display_hash_table_with_chains(hash_table):
    for i in range(len(hash_table)):
        print(i, end=' ')

        for j in hash_table[i]:
            print('-->', end=' ')
            print(j, end=' ')

        print()


def display_hash_table(hash_table):
    for i in range(len(hash_table)):
        print(i, '-->', hash_table[i])
    print()


def find_best_hash_table(hash_tables_list: list):
    max_chain_length_list = []
    for hash_table in hash_tables_list:
        chain_length_list = []
        for cell in hash_table:
            chain_length_list.append(len(cell))
        max_chain_length_list.append(max(chain_length_list))

    return max_chain_length_list.index(min(max_chain_length_list))


if __name__ == '__main__':
    # # linear probing
    # hash_table_with_linear_probing = initialize_hashtable(HASH_TABLE_LENGTH)
    # keys = [random.randint(1, MAX_KEY_VALUE) for i in range(KEYS_NUM)]
    # values = [VALUE_IN_HASH_TABLE_TEMPLATE + str(i) for i in range(KEYS_NUM)]
    # for key, value in zip(keys, values):
    #     insert_into_hash_table_with_linear_probing(hash_table_with_linear_probing, key, value, HASH_CONSTANT_LIST[0])
    # display_hash_table(hash_table_with_linear_probing)

    # # double hashing
    # hash_table_with_double_hashing = initialize_hashtable(HASH_TABLE_LENGTH)
    # keys = [random.randint(1, MAX_KEY_VALUE) for i in range(KEYS_NUM)]
    # values = [VALUE_IN_HASH_TABLE_TEMPLATE + str(i) for i in range(KEYS_NUM)]
    # for key, value in zip(keys, values):
    #     insert_into_hash_table_with_double_hashing(hash_table_with_double_hashing, key, value, HASH_CONSTANT_LIST[0], HASH_CONSTANT_LIST[0])
    # display_hash_table(hash_table_with_double_hashing)

    # # hashing with chains
    hash_tables = []
    for index, HASH_CONSTANT in enumerate(HASH_CONSTANT_LIST):
        print(f'HASH CONSTANT number {index} = {HASH_CONSTANT}')
        for key_index in range(NUM_KEYS_PORTIONS):
            hash_table = initialize_hashtable_with_chains(HASH_TABLE_LENGTH)
            keys = [random.randint(1, MAX_KEY_VALUE) for i in range(KEYS_NUM)]
            values = [VALUE_IN_HASH_TABLE_TEMPLATE + str(i) for i in range(KEYS_NUM)]
            for key, value in zip(keys, values):
                insert_into_hash_table_with_chains(hash_table, key, value, HASH_CONSTANT)
            display_hash_table(hash_table)
            hash_tables.append(hash_table)
        print('-------------------')

    print(f'The best result was in hash table # {find_best_hash_table(hash_tables) // 2}')
