from bitcoinlib.wallets import Wallet, wallet_delete, wallets_list

def remove_all_wallets():
        # List all wallets
        wallet_names = [wallet['name'] for wallet in wallets_list()]
        
        # Delete each wallet
        for wallet_name in wallet_names:
            try:
                wallet_delete(wallet_name)
                print(f"Deleted wallet: {wallet_name}")
            except Exception as e:
                print(f"Failed to delete wallet: {wallet_name}, Error: {e}")

remove_all_wallets()
