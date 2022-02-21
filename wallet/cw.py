import binascii
from pywallet import wallet
from bip_utils import Bip44Coins, Bip44, Monero, MoneroMnemonicGenerator, MoneroWordsNum, MoneroSeedGenerator




def xmr_wallet():

    mnemonic = MoneroMnemonicGenerator().FromWordsNumber(MoneroWordsNum.WORDS_NUM_25)
    seed_bytes = MoneroSeedGenerator(mnemonic).Generate()
    # Create BIP44 object and derive default path
    bip44_def_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.MONERO_ED25519_SLIP).DeriveDefaultPath()

    # Create Monero object from the BIP44 private key -> monero_priv_spend_key = sc_reduce(kekkak256(bip44_priv_key))
    monero = Monero.FromBip44PrivateKey(bip44_def_ctx.PrivateKey().Raw().ToBytes())

    wallet = {'prv_spend': monero.PrivateSpendKey().Raw().ToHex(),
              "prv_view": monero.PrivateViewKey().Raw().ToHex(),
              "pub_spend": monero.PublicSpendKey().RawCompressed().ToHex(),
              "pub_view": monero.PublicViewKey().RawCompressed().ToHex(),
              "main_addr": monero.PrimaryAddress(),
              "sub_addr": monero.Subaddress(1),
             }

    return wallet




def doge_wallet():
    seed = wallet.generate_mnemonic()
    w = wallet.create_wallet(network="DOGE", seed=seed, children=1)
    w["sub_address"] = w['children'][0]['address']
    return w


