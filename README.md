Example Python files for 
Bitcoins the hard way: Using the raw Bitcoin protocol
http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html

These files are for illustration of how the Bitcoin protocol works
and should not be used for real purposes.

docker run -ti --name btcdev -P -p 49020:19000 poliver/bitcoin-dev-box


docker-machine env default --shell cmd
set DOCKER_TLS_VERIFY=1
set DOCKER_HOST=tcp://192.168.99.100:2376
set DOCKER_CERT_PATH=C:\Users\aslaaf\.docker\machine\machines\default
set DOCKER_MACHINE_NAME=default

C:\Users\aslaaf>docker start -i btcdev

make start 
make getinfo

bitcoin-cli -datadir=1 getaddressesbyaccount ""
[
    "mgSMeAgQP97m8G2STrvBdPouUaHxotwFhB"
]

bitcoin-cli -datadir=2 getaddressesbyaccount ""
[
    "n22NLZeQMATUChs2BDPrKC8RJbgHTewjm7"
]


bitcoin-cli -datadir=1 dumpprivkey muwc2rRij1XuJZ5JqsevtjCvqMw9CenJfK
cQn2htJTY9N742onZafmqzPaYtrPEZtFyjxjtWoK2kJznKMAprji


bitcoin-cli -datadir=1 setgenerate true 102
bitcoin-cli -datadir=1 getbalance





bitcoin-cli -datadir=1 sendtoaddress moyDyvi7VeAhZnGEWtvE62PoDdmoRXRRkf 100000
bitcoin-cli -datadir=1 listtransactions

bitcoin-cli -datadir=1 gettransaction f4fb5c3af573c6eea07cf13324c8b587d5178cffd461ff589751cd1db8a0503d
bitcoin-cli -datadir=1 getbalance


bitcoin-cli -datadir=1 dumpprivkey msxdJgRxcSvxc2T71NqneypFcK5orhDrn9


bitcoin-cli -datadir=2 dumpwallet wallet2.txt


bitcoin-cli -datadir=1 listunspent
[
    {
        "txid" : "acf7496e7262fb977e78bd3c0692722b428bf828c8c2033caa859f8ed582f8b1",
        "vout" : 0,
        "address" : "muwc2rRij1XuJZ5JqsevtjCvqMw9CenJfK",
        "scriptPubKey" : "21031906010cdc4cfafc11a4588fe26197c979bd31f76e19d9f4b91b5660838ac9acac",
        "amount" : 50.00000000,
        "confirmations" : 102,
        "spendable" : true
    },
    {
        "txid" : "de75467206c46c43f143d46e6058cdc770b88e767dd4261f3d091cf9b8d94090",
        "vout" : 0,
        "address" : "muwc2rRij1XuJZ5JqsevtjCvqMw9CenJfK",
        "scriptPubKey" : "21031906010cdc4cfafc11a4588fe26197c979bd31f76e19d9f4b91b5660838ac9acac",
        "amount" : 50.00000000,
        "confirmations" : 101,
        "spendable" : true
    }
]
bitcoin-cli -datadir=1 dumpprivkey muwc2rRij1XuJZ5JqsevtjCvqMw9CenJfK
cQFK8Vqwanamn194EscN3zUMyvPTVc39Dubx5BYccvjXjrwS9mBG

bitcoin-cli -datadir=2 getaddressesbyaccount ""
[
    "n22NLZeQMATUChs2BDPrKC8RJbgHTewjm7"
]



cat ./1/regtest/debug.log

bitcoin-cli -datadir=1 sendtoaddress mtv5Zge8zK8r3UCb1ZVC5P3JkDccJEEB21 10
fba339f561dc37abce4a2d5f1a067ab258375a29a9ee7c202e05989080421ff8
bitcoin-cli -datadir=1 getrawmempooldbalance8zK8r3UCb1ZVC5P3JkDccJEEB21 10000
[
    "fba339f561dc37abce4a2d5f1a067ab258375a29a9ee7c202e05989080421ff8"
]

bitcoin-cli -datadir=1 gettransaction fba339f561dc37abce4a2d5f1a067ab258375a29a9ee7c202e05989080421ff8



