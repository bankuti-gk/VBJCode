import random
import string
from utilities import search
import os

def create_process(cluster_path):
    computer = search.get_computer(cluster_path)
    computer_path = os.path.join(cluster_path, computer)
    cluster_data = search.get_cluster_data(cluster_path)
    processes = search.get_computer_data(computer_path)

    