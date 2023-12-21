from web3 import Web3
from tronpy import Tron
from tronpy.providers import HTTPProvider
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from timeout_decorator import timeout

sender_email = "support@chainsecurity.asia"
receiver_email = "patrickwu8894@gmail.com"
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

GET_BLOCK_API_KEY= "863d14d9-45b8-402f-9a71-e8074c32e5d9"

# SOLANA_RPC_ENDPOINT = "https://silent-radial-firefly.solana-mainnet.quiknode.pro/c841ea6b152f7e3333cb562cbdccb6a5bdae70ed/"
# SOLANA_RPC_ENDPOINT_2 = "https://rpc.ankr.com/solana"
# SOLANA_RPC_ENDPOINT_3 = "https://rpc.ankr.com/solana"

TRON_RPC_ENDPOINT = "6ead3e57-159f-4f34-af2f-f5252099712a"
TRON_RPC_ENDPOINT_2 = GET_BLOCK_API_KEY
TRON_RPC_ENDPOINT_3 = "e63e092c-cd58-4d75-923e-35195c143e85"

ETHEREUM_RPC_ENDPOINT = f'https://eth.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
ETHEREUM_RPC_ENDPOINT_2 = 'https://1rpc.io/eth'
ETHEREUM_RPC_ENDPOINT_3 = 'https://mainnet.infura.io/v3/09e29404c810497ca4d3cee5d9a48bc6'

ARBITRUM_RPC_ENDPOINT = "https://spring-flashy-resonance.arbitrum-mainnet.quiknode.pro/d7f3d3a5d4680be8a6bb64d095bc26267036c41c/"
ARBITRUM_RPC_ENDPOINT_2 = "https://rpc.ankr.com/arbitrum"
ARBITRUM_RPC_ENDPOINT_3 = f'https://arb.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'

AVALANCHE_RPC_ENDPOINT = 'https://avalanche-mainnet.infura.io/v3/8ebddfe9ff214f4b876671eded2260af'
AVALANCHE_RPC_ENDPOINT_2 = 'https://api.avax.network/ext/bc/C/rpc'
AVALANCHE_RPC_ENDPOINT_3 = f'https://avax.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'

BSC_RPC_ENDPOINT = "https://necessary-hardworking-wish.bsc.quiknode.pro/e56058143e8029adf6f8718d20cf5d35dee17750/"
BSC_RPC_ENDPOINT_2 = "https://bsc-dataseed.binance.org/"
BSC_RPC_ENDPOINT_3 = f'https://bsc.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'

CELO_RPC_ENDPOINT = 'https://rpc.ankr.com/celo'
CELO_RPC_ENDPOINT_2 = 'https://forno.celo.org'
CELO_RPC_ENDPOINT_3 = 'https://1rpc.io/celo'

CRONOS_RPC_ENDPOINT = f'https://cro.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
CRONOS_RPC_ENDPOINT_2 = 'https://evm-cronos.crypto.org'
CRONOS_RPC_ENDPOINT_3 = 'https://api.securerpc.com/v1'

ETHEREUM_CLASSIC_RPC_ENDPOINT = f'https://etc.getblock.io/{GET_BLOCK_API_KEY}/mainnet/'
ETHEREUM_CLASSIC_RPC_ENDPOINT_2 = 'https://ethereumclassic.network'
ETHEREUM_CLASSIC_RPC_ENDPOINT_3 = 'https://ethereumclassic.network'

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

node_error_list = []

def main():
    check_eth_connection(ETHEREUM_RPC_ENDPOINT)
    check_eth_connection(ETHEREUM_RPC_ENDPOINT_2)
    check_eth_connection(ETHEREUM_RPC_ENDPOINT_3)

    check_eth_connection(ARBITRUM_RPC_ENDPOINT)
    check_eth_connection(ARBITRUM_RPC_ENDPOINT_2)
    check_eth_connection(ARBITRUM_RPC_ENDPOINT_3)

    check_eth_connection(AVALANCHE_RPC_ENDPOINT)
    check_eth_connection(AVALANCHE_RPC_ENDPOINT_2)
    check_eth_connection(AVALANCHE_RPC_ENDPOINT_3)

    check_eth_connection(BSC_RPC_ENDPOINT)
    check_eth_connection(BSC_RPC_ENDPOINT_2)
    check_eth_connection(BSC_RPC_ENDPOINT_3)

    check_eth_connection(CELO_RPC_ENDPOINT)
    check_eth_connection(CELO_RPC_ENDPOINT_2)
    check_eth_connection(CELO_RPC_ENDPOINT_3)

    check_eth_connection(CRONOS_RPC_ENDPOINT)
    check_eth_connection(CRONOS_RPC_ENDPOINT_2)
    check_eth_connection(CRONOS_RPC_ENDPOINT_3)

    check_eth_connection(ETHEREUM_CLASSIC_RPC_ENDPOINT)
    check_eth_connection(ETHEREUM_CLASSIC_RPC_ENDPOINT_2)
    check_eth_connection(ETHEREUM_CLASSIC_RPC_ENDPOINT_3)

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

    # print(node_error_list)
    if (len(node_error_list) > 0):
        send_error_email()


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

if __name__ == "__main__":
    main()