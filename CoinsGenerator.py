from k_amino import Client, SubClient
import time

community_link = "http://aminoapps.com/c/Heaven_999"
email = "seuemail@gmail.com"
password = "suasenha"

client = Client()
from_info = client.get_from_link(community_link)
from_id = from_info.comId

client.login(email, password)
client.join_community(comId=from_id)

from_client = SubClient(comId=from_id)

for i in range(24):
    from_client.send_active_time()
    print(f"{i + 1} Coin Generating - OK")
    time.sleep(9)
