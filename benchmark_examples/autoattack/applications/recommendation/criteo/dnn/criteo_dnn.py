# Copyright 2023 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List, Optional

import torch
import torch.nn as nn
from torchmetrics import AUROC, Accuracy, Precision

from benchmark_examples.autoattack.applications.recommendation.criteo.criteo_base import (
    CriteoBase,
)
from secretflow.ml.nn.applications.sl_dnn_torch import DnnBase, DnnFuse
from secretflow.ml.nn.utils import TorchModel, metric_wrapper, optim_wrapper


class CriteoDnn(CriteoBase):
    def __init__(self, config, alice, bob, hidden_size=64):
        super().__init__(
            config,
            alice,
            bob,
            epoch=3,
            train_batch_size=512,
            hidden_size=hidden_size,
            dnn_base_units_size_alice=[200, 100, hidden_size],
            dnn_base_units_size_bob=[200, 100, hidden_size],
            dnn_fuse_units_size=[64, 1],
            dnn_embedding_dim=16,
        )

    def create_base_model_alice(self):
        return TorchModel(
            model_fn=DnnBase,
            loss_fn=nn.BCELoss,
            optim_fn=optim_wrapper(torch.optim.Adam, lr=1e-2),
            metrics=[
                metric_wrapper(Accuracy, task="binary"),
                metric_wrapper(AUROC, task="binary"),
            ],
            input_dims=self.alice_input_dims,
            dnn_units_size=self.dnn_base_units_size_alice,
            sparse_feas_indexes=self.alice_sparse_indexes,
            embedding_dim=self.dnn_embedding_dim,
        )

    def create_base_model_bob(self):
        return TorchModel(
            model_fn=DnnBase,
            loss_fn=nn.BCELoss,
            optim_fn=optim_wrapper(torch.optim.Adam, lr=1e-2),
            metrics=[
                metric_wrapper(Accuracy, task="binary"),
                metric_wrapper(AUROC, task="binary"),
            ],
            # input_dims=[1 for _ in range(26)],
            input_dims=self.bob_input_dims,
            dnn_units_size=self.dnn_base_units_size_bob,
            sparse_feas_indexes=self.bob_sparse_indexes,
            embedding_dim=self.dnn_embedding_dim,
        )

    def create_fuse_model(self):
        return TorchModel(
            model_fn=DnnFuse,
            loss_fn=nn.BCELoss,
            optim_fn=optim_wrapper(torch.optim.Adam, lr=1e-2),
            metrics=[
                metric_wrapper(Accuracy, task="binary"),
                metric_wrapper(Precision, task="binary"),
                metric_wrapper(AUROC, task="binary"),
            ],
            input_dims=[self.hidden_size, self.hidden_size],
            dnn_units_size=self.dnn_fuse_units_size,
            output_func=nn.Sigmoid,
        )

    def support_attacks(self):
        return ['norm', 'replay', 'replace', 'exploit']

    def dnn_base_units_size_range_alice(self) -> Optional[list]:
        return [[200, 100, -1]]

    def dnn_base_units_size_range_bob(self) -> Optional[list]:
        return None

    def dnn_fuse_units_size_range(self) -> Optional[list]:
        return [[64, 1]]

    def dnn_embedding_dim_range(self) -> Optional[List[int]]:
        return [16]
