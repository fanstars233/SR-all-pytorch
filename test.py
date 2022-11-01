import torch
from torch.utils.data import DataLoader
from dataset.data import get_training_set, get_test_set
from DBPN.model import DBPN, DBPNS, DBPNLL

# train_set = get_training_set(4)
# test_set = get_test_set(4)
# training_data_loader = DataLoader(
#     dataset=train_set, batch_size=2, shuffle=True)
# testing_data_loader = DataLoader(
#     dataset=test_set, batch_size=2, shuffle=False)

model = DBPN(num_channels=3, base_channels=64, feat_channels=256, num_stages=7,
                    scale_factor=4)
model.weight_init()
model = torch.nn.DataParallel(model, device_ids=range(1))
model.load_state_dict(torch.load('DBPN_/DBPN_x4.pth', map_location=lambda storage, loc: storage))
