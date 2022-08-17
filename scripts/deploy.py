from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3

def deploy_fund_me():
  account = get_account()
  #pass the price feed to the fundeme contract
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
  else:
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address
    
  fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify")),
  print(f"Contract deployed to {fund_me[-1].address}")
  #returning the most recent contract object so we can use it to write the test
  return fund_me[-1]



def main():
  deploy_fund_me()