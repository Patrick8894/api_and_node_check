from web3 import Web3
from tronpy import Tron
from tronpy.providers import HTTPProvider
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from timeout_decorator import timeout
from solana.rpc.api import Client

sender_email = "support@chainsecurity.asia"
receiver_email = "yize@chainsecurity.asia"
subject = "Node Connection Error"
# body = "API Response is not valid!"

smtp_server = "email-smtp.us-west-2.amazonaws.com"
smtp_port = 587
email_username = "AKIAS7ZPBOAL3NP6M47X"
email_password = "BJE4alkKMjQeebGhz4RQlXOlGofZfPiygmlIlvRM3Tco"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.attach(MIMEText(body, "plain"))

# 以下是各個節點的網址(network: ETHERREUM, TRON, BSC, ARBITRUM, AVALANCHE, CELO, CRONOS, ETC, ETHEREUM_POW, FANTOM, OPTIMISM, POLYGON, SOLANA)
GET_BLOCK_API_KEY= "863d14d9-45b8-402f-9a71-e8074c32e5d9"

ETHEREUM_RPC_ENDPOINT = f'https://eth.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
ETHEREUM_RPC_ENDPOINT_2 = 'https://1rpc.io/eth'
ETHEREUM_RPC_ENDPOINT_3 = 'https://mainnet.infura.io/v3/09e29404c810497ca4d3cee5d9a48bc6'
ETHEREUM_RPC_ENDPOINT_4 = 'https://go.getblock.io/0d973a41b49246eb8d62eb319b127c5d'

TRON_RPC_ENDPOINT = "6ead3e57-159f-4f34-af2f-f5252099712a"
TRON_RPC_ENDPOINT_2 = "36fe9289-bed3-469e-af6c-5acdc7ba68f9"
TRON_RPC_ENDPOINT_3 = "e63e092c-cd58-4d75-923e-35195c143e85"

BSC_RPC_ENDPOINT = "https://multi-lingering-dew.bsc.quiknode.pro/02c1eb584814899041fd06b1241698d301872d9b/"
BSC_RPC_ENDPOINT_2 = "https://bsc-dataseed.binance.org/"
BSC_RPC_ENDPOINT_3 = f'https://bsc.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
BSC_RPC_ENDPOINT_4 = f'https://go.getblock.io/41ad6b0d79ad492ca551019a9a47b304'

ARBITRUM_RPC_ENDPOINT = "https://old-cool-glitter.arbitrum-mainnet.quiknode.pro/135389a3f7dbb305a14df541190b73cd2abf4fa0/"
ARBITRUM_RPC_ENDPOINT_2 = "https://rpc.ankr.com/arbitrum"
ARBITRUM_RPC_ENDPOINT_3 = f'https://arb.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'

# avalanche getblock 節點有問題(2023.12.22)
AVALANCHE_RPC_ENDPOINT = 'https://avalanche-mainnet.infura.io/v3/8ebddfe9ff214f4b876671eded2260af'
AVALANCHE_RPC_ENDPOINT_2 = 'https://api.avax.network/ext/bc/C/rpc'
# AVALANCHE_RPC_ENDPOINT_3 = 'https://go.getblock.io/63cef2c9e8ff4aec9830af9078f2d593'

CELO_RPC_ENDPOINT = 'https://rpc.ankr.com/celo'
CELO_RPC_ENDPOINT_2 = 'https://forno.celo.org'
CELO_RPC_ENDPOINT_3 = 'https://1rpc.io/celo'

# cronos getblock 節點有問題(2023.12.22)
CRONOS_RPC_ENDPOINT = 'https://evm-cronos.crypto.org'
CRONOS_RPC_ENDPOINT_2 = 'https://api.securerpc.com/v1'

# ETHEREUM_CLASSIC 目前只有getblock可以正常使用
ETHEREUM_CLASSIC_RPC_ENDPOINT = f'https://etc.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'

ETHEREUM_POW_RPC_ENDPOINT = 'https://mainnet.ethereumpow.org'
ETHEREUM_POW_RPC_ENDPOINT_2 = 'https://mainnet.ethereumpow.org'
ETHEREUM_POW_RPC_ENDPOINT_3 = 'https://mainnet.ethereumpow.org'

FANTOM_RPC_ENDPOINT = f'https://ftm.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
FANTOM_RPC_ENDPOINT_2 = 'https://rpc.ftm.tools/'
FANTOM_RPC_ENDPOINT_3 = 'https://fantom.api.onfinality.io/public'

OPTIMISM_RPC_ENDPOINT = f'https://op.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
OPTIMISM_RPC_ENDPOINT_2 = 'https://mainnet.optimism.io'
OPTIMISM_RPC_ENDPOINT_3 = 'https://mainnet.optimism.io'

POLYGON_RPC_ENDPOINT = f'https://matic.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
POLYGON_RPC_ENDPOINT_2 = 'https://polygon-rpc.com'
POLYGON_RPC_ENDPOINT_3 = 'https://polygon.api.onfinality.io/public'

SOLANA_RPC_ENDPOINT = "https://falling-clean-sponge.solana-mainnet.quiknode.pro/dad6c066a36249ae386087268c0c9626a4ca316e/"
SOLANA_RPC_ENDPOINT_2 = "https://attentive-skilled-patina.solana-mainnet.quiknode.pro/6695ae703cb35d46527304d4f7a92d7495db01aa/"

node_error_list = []

def main():
    
    check_eth_connection(ETHEREUM_RPC_ENDPOINT)
    check_eth_connection(ETHEREUM_RPC_ENDPOINT_2)
    check_eth_connection(ETHEREUM_RPC_ENDPOINT_3)
    check_eth_connection(ETHEREUM_RPC_ENDPOINT_4)

    check_eth_connection(ARBITRUM_RPC_ENDPOINT)
    check_eth_connection(ARBITRUM_RPC_ENDPOINT_2)
    check_eth_connection(ARBITRUM_RPC_ENDPOINT_3)

    check_eth_connection(AVALANCHE_RPC_ENDPOINT)
    check_eth_connection(AVALANCHE_RPC_ENDPOINT_2)
    # check_eth_connection(AVALANCHE_RPC_ENDPOINT_3)

    check_eth_connection(BSC_RPC_ENDPOINT)
    check_eth_connection(BSC_RPC_ENDPOINT_2)
    check_eth_connection(BSC_RPC_ENDPOINT_3)
    check_eth_connection(BSC_RPC_ENDPOINT_4)

    check_eth_connection(CELO_RPC_ENDPOINT)
    check_eth_connection(CELO_RPC_ENDPOINT_2)
    check_eth_connection(CELO_RPC_ENDPOINT_3)

    check_eth_connection(CRONOS_RPC_ENDPOINT)
    check_eth_connection(CRONOS_RPC_ENDPOINT_2)
    # check_eth_connection(CRONOS_RPC_ENDPOINT_3)

    check_eth_connection(ETHEREUM_CLASSIC_RPC_ENDPOINT)
    # check_eth_connection(ETHEREUM_CLASSIC_RPC_ENDPOINT_2)
    # check_eth_connection(ETHEREUM_CLASSIC_RPC_ENDPOINT_3)

    check_eth_connection(ETHEREUM_POW_RPC_ENDPOINT)
    check_eth_connection(ETHEREUM_POW_RPC_ENDPOINT_2)
    check_eth_connection(ETHEREUM_POW_RPC_ENDPOINT_3)

    check_eth_connection(FANTOM_RPC_ENDPOINT)
    check_eth_connection(FANTOM_RPC_ENDPOINT_2)
    check_eth_connection(FANTOM_RPC_ENDPOINT_3)

    check_eth_connection(OPTIMISM_RPC_ENDPOINT)
    check_eth_connection(OPTIMISM_RPC_ENDPOINT_2)
    check_eth_connection(OPTIMISM_RPC_ENDPOINT_3)

    check_eth_connection(POLYGON_RPC_ENDPOINT)
    check_eth_connection(POLYGON_RPC_ENDPOINT_2)
    check_eth_connection(POLYGON_RPC_ENDPOINT_3)

    check_tron_connection(TRON_RPC_ENDPOINT)
    check_tron_connection(TRON_RPC_ENDPOINT_2)
    check_tron_connection(TRON_RPC_ENDPOINT_3)

    check_solana_connection(SOLANA_RPC_ENDPOINT)
    check_solana_connection(SOLANA_RPC_ENDPOINT_2)

    # print(node_error_list)
    if (len(node_error_list) > 0):
        send_error_email()
    else:
        print("All nodes successfully connected!")


def check_eth_connection(api_url):
    w3 = Web3(Web3.HTTPProvider(api_url))
    is_connected = w3.is_connected()
    print(f'checking {api_url}...')
    if (not is_connected):
        # send_error_email(f'{api_url} Node not connected!')
        node_error_list.append(api_url)
        print(f'{api_url} Node not connected!')
    


def send_error_email():
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_username, email_password)
        error_message = "Node connection error!\n"
        error_message += "\n".join(node_error_list)
        message.attach(MIMEText(error_message, "plain"))
        print(error_message)
        server.sendmail(sender_email, receiver_email, message.as_string())

def check_tron_connection(api_url):
    print(f'checking {api_url}...')
    try:
        check_tron_connection_in_time(api_url)
    except TimeoutError:
        print(f'{api_url} Node not connected!')
        node_error_list.append(api_url)
        # send_error_email(f'{api_url} Node not connected!')

@timeout(10)
def check_tron_connection_in_time(api_url):
    client = Tron(HTTPProvider(api_key="6ead3e57-159f-4f34-af2f-f5252099712a"))

def check_solana_connection(api_url):
    print(f'checking {api_url}...')
    try:
        client = Client(api_url)
        client.get_slot()
    except:
        print(f'{api_url} Node not connected!')
        node_error_list.append(api_url)
        # send_error_email(f'{api_url} Node not connected!')

if __name__ == "__main__":
    main()