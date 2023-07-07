from PackageDelvery.src.hashtable import HashTable
from PackageDelvery.src.load_data import loadPackageData


def main():
    hashTable = HashTable(40)
    loadPackageData(hashTable)
    assert len(hashTable.table) == 40  # Replace 40 with the number of packages in your CSV file


if __name__ == "__main__":
    main()
