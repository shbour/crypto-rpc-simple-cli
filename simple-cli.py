from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from pprint import pprint

conn = AuthServiceProxy("http://USER:PASS@IP_ADDR:PORT")

def simpleCli():
    account = ""
    userinput = input("What do you want to do? ")
    
    if userinput == "help" or userinput == "h":
        print("add node: Allows you to add nodes by their IP" + \n
        "remove node: Allows you to remove nodes by their IP" + \n
        "try node: Allows you to try to connect to a node one time" + \n
        "backup: Requests a directory path to store the wallet backup" + \n
        "multisig: Allows you to create a multisig address with two (2) keys" + \n
        "create raw tx: Allows you to create a raw transaction (Information is asked one at a time)" + \n
        "decode tx: Decrypt the tx with the 'hex string' of the transaction" + \n
        "show private key: Will ask for the address you want to get the private key for" + \n
        "name of address: Will get you the account name of the address given" + \n
        "show all keys: Requests a directory to send a file with all the private keys in the wallet" + \n
        "get account address: Will give you the address of the account name given" + \n
        "encrypt: Requests a password to encrypt the wallet (Highly recommended)" + \n
        "get node info: Will give you the information on your nodes" + \n
        "bal: Will show total wallet balance" + \n
        "acc bal: (or account balance) will show your balance by account name (shbour 40XP jhon 5XP)" + \n
        "get addr by acc: (or get addresses by account) will show you the addresses related to that account name" + \n
        "bal by addr: (or balance by address) Will show the balance to the specified address" + \n
        "best block hash: Will show the best block hash" + \n
        "block: (or get block) Requests a block hash to display block info" + \n
        "block count: (or get block count) Displays the longuest chain" + \n
        "hash: Requests block index (index 0 is genesis block) to display block hash" + \n
        "connections: Shows the amount of peers you are connected to" + \n
        "difficulty: Displays the difficulty levels" + \n
        "info: Displays your wallet info" + \n
        "mining info: Displays your mining information" + \n
        "new addr: (or new address) Will generate a new address for the account given" + \n
        "peers: Displays the info of your peers" + \n
        "raw pool: (or getrawpool) will show you the raw value of the memory pool (transaction pool/queue)" + \n
        "raw tx: (or get raw transaction) displays the raw transaction value of a TXID" + \n
        "received by account: Display the amount of coins that wagered into the address(es) to the specified account name" + \n
        "received by address: Display the amount of coins that wagered into the address" + \n
        "unspent coins: Will show your the coins that has not been spent in your wallet" + \n
        "add priv key: (or import priv key) Allows you to import an address from another wallet or a paper wallet to the current wallet by entering the private key of the wanted address" + \n
        "dismiss block: (or void block) Requests the hash of the block that is being voided" + \n
        "key refill: refills the keys in your key pool" + \n
        "show accounts: Will display a list of account" + \n
        "cc: (or coincontrol) will display the accounts by groups of addresses" + \n
        "received addresses: Will display a list of addresses your received funds with" + \n
        "send from: (or send with) Requests a source account name or address, a destination address and the amount to be sent" + \n
        "send raw tx: Requests the hexstring of the transaction" + \n
        "withdraw: (or sendtoaddress) Allows you to send coins from your total balance to another address" + \n
        "setaccount: Requests for a account name and address" + \n
        "sign message: (or signmessage) Requests an address to sign the message with, and the message itself to be signed" + \n
        "stop: (or kill) will terminate the daemon (back-end) of the wallet and will require a manual closure of the GUI (Graphical User Interface)" + \n
        "create block: (or submit block) Requests the hexdata of the block to be created" + \n
        "valid addr: (or valid address) Requests an address to verify its authenticity with the current blockchain" + \n
        "verify message: (or verifymessage) Allows you to verify a message to see if its true or false (form of authentication") + \n
        "lock: (or walletlock) will lock your wallet if it was unlocked (Needs to have a password to be locked)" + \n
        "unlock: (or walletpassphrase) requests a password and a time in days to have the wallet unlocked (100% unlock, not secure") + \n
        "change password: (or walletpassphrasechange) Requests the old password before asking for the new password)"
             
    if userinput == "add node" or userinput == "addnode" or userinput == "addnode add":
        ip, add = [str(x) for x in input("Enter the IP or URL of the desired node (127.0.0.1 add): ").split()]
        if ip != "":
            conn.addnode(ip, "add")
            print("The node was added to the list successfully")
            simpleCli()
        else:
            print("You did not write anything")
            simpleCli()

    elif userinput == "remove node" or userinput == "delete node" or userinput == "addnode remove" or userinput == "del node" or userinput == "rm node":
        ip, remove = [str(x) for x in input("Enter the IP or the URL of the undesired node (127.0.0.1 remove): ").split()]
        if ip != "":
            conn.addnode(ip, "remove")
            print("The node was removed to the list successfully")
            simpleCli()
        else:
            print("You did not write anything")
            simpleCli()

    elif userinput == "try node" or userinput == "onetry" or userinput == "addnode onetry":
        ip, onetry = [str(x) for x in input("Enter the IP or URL of the node you want to try: ").split()]
        if ip != "":
            if onetry != "":
                conn.addnode(ip, "onetry")
                print("The node has been tried successfully")
                simpleCli()
            else:
                print('You forgot to add "onetry"')
                simpleCli()
        else:
            print("You did not write anything")
            simpleCli()

    elif userinput == "backup" or userinput == "backup wallet":
        dist = input("Enter the full path for the wallet backup, ending by the file's name and extension: ")
        conn.backupwallet(dist)
        simpleCli()

    elif userinput == "create multisig" or userinput == "multisig":
        req = input(int("Enter the amount of the required keys"))
        key1, key2 = [int(x) for x in input("Enter both keys seperated by a space ").split()]
        print(conn.createmultisig(req + ' [' + key1 + ',' + key2 + ']'))
        simpleCli()

    elif userinput == "create raw tx" or userinput == "create raw transaction" or userinput == "createrawtx" or userinput == "createrawtransaction":
        txid = input("Enter Transaction ID (txid): ")
        n = input("Enter 'vout' value: ")
        address = input("Enter the receiving address: ")
        amount = int(input("Enter the amount of coins to send: "))
        print(conn.createrawtransaction('[{"txid":' + txid + ',"vout":' + n + '}]' + " {" + address + ":" + amount + "}"))

    elif userinput == "decode tx" or userinput == "decode raw tx" or userinput == "decoderawtransaction":
        hexstring = input('Enter the "hex string" of the transaction: ')
        print(conn.decoderawtransaction(hexstring))
        simpleCli()

    elif userinput == "show private key" or userinput == "dump private key" or userinput == "dumpprivkey" or userinput == "private key":
        address = input("Enter the desired address: ")
        print(conn.dumpprivkey(address))
        simpleCli()

    elif userinput == "dumpwallet" or userinput == "show all keys" or userinput == "dump private keys":
        dest = input("Enter the full path of the wallet private keys file: ")
        conn.dumpwallet(dest)
        print("File sent to " + dest)
        simpleCli()

    elif userinput == "encrypt" or userinput == "encryptwallet" or userinput == "create password":
        try:
            password = input("Enter your encryption password here: ")
            conn.encryptwallet(password)
            simpleCli()
        except ValueError:
            print("You had an error writing the password")
            simpleCli()

    elif userinput == "name of address" or userinput == "account name" or  userinput =="get account" or userinput == "getaccount" or userinput == "address name":
        addr = input("Enter the desired account address to learn its account name: ")
        print(conn.getaccount(addr))
        simpleCli()

    elif userinput == "get account address" or userinput == "account address" or userinput == "account addr" or userinput == "acc addr":
        address = input("Enter the account you wish to get the address for: ")
        print(conn.getaccountaddress(address))
        simpleCli()

    elif userinput == "getaddednodeinfo" or userinput == "get added node info" or userinput == "get node info" or userinput == "new node info" or userinput == "added node info":
        print(conn.getaddednodeinfo(True))
        simpleCli()
    
    elif userinput == "getaddressesbyaccount" or userinput == "get addresses by account" or userinput == "get addr by acc" or userinput == "get addr by account":
        addresses = input("Enter the desired account: ")
        print(conn.getaddressesbyaccount(addresses))
        simpleCli()
        
    elif userinput == "bal" or userinput == "balance":
        print(conn.getbalance())
        simpleCli()

    elif userinput == "bal by account" or userinput == "account balance" or userinput == "account bal" or userinput == "acc bal":
        account = input("Which account would you wish to see the balance from?: ")
        print(conn.getbalance(account))
        simpleCli()

    elif userinput == "bal by address" or userinput == "address balance" or userinput == "addr bal":
        addr = input("From which address would you wish to see the balance from?: ")
        account = conn.getaccount(addr)
        print(conn.getbalance(account))
        simpleCli()

    elif userinput == "getbestblockhash" or userinput == "get best block hash" or userinput == "best block hash":
        print(conn.getbestblockhash())
        simpleCli()

    elif userinput == "getblock" or userinput == "get block" or userinput == "block":
        blockhash = input("Enter the hash the the desired block: ")
        pprint(conn.getblock(blockhash))
        simpleCli()

    elif userinput == "getblockcount" or userinput == "block count" or userinput == "get block count" or userinput == "longest chain" or userinput == "long chain" or userinput == "biggest block" or userinput == "longest blockchain" or userinput == "biggest blockchain":
        print(conn.getblockcount())
        simpleCli()

    elif userinput == "getblockhash" or userinput == "get block hash" or userinput == "get hash" or userinput == "hash":
        hashblock = int(input("Enter the index (index 0 is genesis block) of the block hash you desire: "))
        print(conn.getblockhash(hashblock))
        simpleCli()

    elif userinput == "getblocktemplate" or userinput == "get block template" or userinput == "block template":
        print("Not available in this version")
        simpleCli()
  
    elif userinput == "connections" or userinput == "getconnections" or userinput == "count connections" or userinput == "count connect" or userinput == "count connected":
        print(conn.getconnectioncount())
        simpleCli()
  
    elif userinput == "difficulty":
        pprint(conn.getdifficulty())
        simpleCli()

    #Does not work if not PoW
    elif userinput == "gen" or userinput == "get generate" or userinput == "is generating":
        print(conn.getgenerate())
        simpleCli()

    #Does not work if not mining (generating)
    elif userinput == "hashrate" or userinput == "hash rate" or userinput == "get hash per sec" or userinput == "gethashespersec" or userinput == "get rate":
        print(conn.gethashespersec())
        simpleCli()

    elif userinput == "info" or userinput == "getinfo":
        pprint(conn.getinfo())
        simpleCli()
  
    elif userinput == "mininginfo" or userinput == "mining info" or userinput == "getmininginfo":
        pprint(conn.getmininginfo())
        simpleCli()

    elif userinput == "getnewaddress" or userinput == "create new address" or userinput == "new address" or userinput == "new addr":
        account = input("Enter account name of the address, enter nothing for no name: ")
        print("Your new address is:" + conn.getnewaddress(account))
        simpleCli()
  
    elif userinput == "peers" or userinput == "get peer info" or userinput == "getpeerinfo" or userinput == "show peers" or userinput == "display peers":
        pprint(conn.getpeerinfo())
        simpleCli()
  
    elif userinput == "getrawchangeaddress" or userinput == "get raw change address" or userinput == "raw change addr":
        print("Not available")
        simpleCli()

    elif userinput == "getrawmempool" or userinput == "rawmempool" or userinput == "raw mem pool" or userinput == "raw pool" or userinput == "raw mem":
        pprint(conn.getrawmempool())
        simpleCli()

    elif userinput == "getrawtransaction" or userinput == "raw transaction" or userinput == "raw tx" or userinput == "raw txid":
        txid = input("Enter the txid of the desired transaction: ")
        pprint(conn.getrawtransaction(txid))
        simpleCli()

    elif userinput == "getreceivedbyaccount" or userinput == "received by account":
        account = input("Enter the accont you want to see the total received amount: ")
        print(conn.getreceivedbyaccount(account))
        simpleCli()

    elif userinput == "getreceivedbyaddress" or userinput == "get received by address" or userinput == "how much by address" or userinput == "received by address":
        address = input("Enter the address you want to see the total received amount: ")
        print(conn.getreceivedbyaddress(address))
        simpleCli()

    elif userinput == "gettransaction" or userinput == "get transaction" or userinput == "get tx":
        txid = input("Enter the tx id of the transaction you want to view: ")
        pprint(conn.gettransaction(txid))
        simpleCli()
  
    elif userinput == "unspent coins" or userinput == "unspent tx" or userinput == "gettxoutsetinfo" or userinput == "get output tx info":
        pprint.pprint(conn.gettxoutsetinfo())
        simpleCli()

    elif userinput == "importprivkey" or userinput == "import priv key" or userinput == "add priv key" or userinput == "add private key":
        privkey = input("Enter private key to import: ")
        print("Added private key: " + conn.importprivkey(privkey))
        print("Private key has been added")
        simpleCli()

    elif userinput == "invalidateblock" or userinput == "null block" or userinput == "void block" or userinput == "dismiss block":
        blockhash = input("Enter the hash of the block to invalidate: ")
        print(conn.invalidateblock(blockhash))
        simpleCli()

    elif userinput == "refill pool" or userinput == "keypoolrefill" or userinput == "key pool refill" or userinput == "key refill":
        conn.keypoolrefill()
        simpleCli()
  
    elif userinput == "accounts name" or userinput == "show accounts" or userinput == "list accounts" or userinput == "listaccounts":
        pprint(conn.listaccounts())
        simpleCli()
        
    elif userinput == "address group" or userinput == "coincontrol" or userinput == "cc" or userinput == "listaddressgroupings" or userinput == "list address groupings":
        pprint(conn.listaddressgroupings())
        simpleCli()
        
    elif userinput == "received addresses" or userinput == "received addr" or userinput == "recept addr" or userinput == "recept addresses" or userinput == "listreceivedbyaddress":
        pprint(conn.listreceivedbyaddress())
        simpleCli()

    elif userinput == "sendfrom" or userinput == "send from" or userinput == "send with":
        account = input("Enter address or account you desire to spend with: ")
        address = input("Enter the receiving address: ")
        amount = int(input("Enter the desired amount to send: "))
        pprint(conn.sendfrom(account, address, amount))
        simpleCli()

    elif userinput == "sendrawtransaction" or userinput == "send raw tx" or userinput == "send raw transaction":
        hexstring = input("Enter the hexstring of the raw transaction: ")
        pprint(conn.sendrawtransaction(hexstring))
        simpleCli()

    elif userinput == "sendtoaddress" or userinput == "send to address" or userinput == "withdraw":
        address = input("Enter the receiving address: ")
        amount = int(input("Enter the amount to send: "))
        pprint("This is the txid of the transaction: " + conn.sendtoaddress(address, amount))
        simpleCli()

    #Changes the address name and adds a new address with the older account name
    elif userinput == "setaccount" or userinput == "set account" or userinput == "gen account" or userinput == "generate account" or userinput == "create account":
        address, account = [str(x) for x in input("Enter the address and the account name: ").split()]
        print(conn.setaccount(address, account))
        simpleCli()

    elif userinput == "signmessage" or userinput == "sign message" or userinput == "auth message":
        addr = input("Enter addr to the person that will receive the message: ")
        msg = input("Enter message here: \n\t")
        print(conn.signmessage(addr, msg))
        simpleCli()

    elif userinput == "stop" or userinput == "kill":
        conn.stop()

    elif userinput == "submitblock" or userinput == "send block" or userinput == "create block":
        hexdata = input("Enter the hex data of the block creation: ")
        pprint(conn.submitblock(hexdata))
        simpleCli()

    elif userinput == "validateaddress" or userinput == "valid address" or userinput == "valid addr":
        addr = input("Enter address to verify: ")
        pprint(conn.validateaddress(addr))
        simpleCli()
            
    elif userinput == "verifymessage" or userinput == "verify message":
        address, msg = [str(x) for x in input("Enter the address and the message: ").split()]
        conn.verifymessage(address, msg)
        simpleCli()

    elif userinput == "walletlock" or userinput == "lock wallet" or userinput == "lock":
        conn.walletlock()
        print("Wallet has been locked")
        simpleCli()

    elif userinput == "walletpassphrase" or userinput == "unlock wallet" or userinput == "unlock":
        password = input("Enter wallet encryption password: ")
        timeout = int(input("Enter how long in second you want to keep the wallet unlocked?: "))
        conn.walletpassphrase(password, timeout)
        print("You have unlocked the wallet for " + (timeout * 60 * 60 * 24) + " days!")
        simpleCli()

    elif userinput == "":
        print("You did not enter anything\n")
        simpleCli()

    elif userinput == "change password" or userinput == "change passphrase" or userinput == "walletpassphrasechange":
        oldpassphrase, newpassphrase = [str(x) for x in input("Enter old password and then new password ").split()]
        while True:
            if oldpassphrase == "":
                print("Enter old password: ")
            elif newpassphrase == "":
                print("Enter new password: ")
            else: 
                conn.walletpassphrasechange(oldpassphrase, newpassphrase)
                print("Password updated!")
                simpleCli()

simpleCli()
