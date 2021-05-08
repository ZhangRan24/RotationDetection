# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os
import sys
sys.path.append("../../")

from libs.models.detectors.gwd import build_whole_network
from tools.test_msra_td500_base import TestIMSRATD500
from libs.configs import cfgs


class TestMSRATD500GWD(TestIMSRATD500):

    def eval(self):
        txt_name = '{}.txt'.format(self.cfgs.VERSION)
        real_test_img_list = self.get_test_image()

        gwd = build_whole_network.DetectionNetworkGWD(cfgs=self.cfgs,
                                                      is_training=False)
        self.test_msra_td500(det_net=gwd, real_test_img_list=real_test_img_list, txt_name=txt_name)

        if not self.args.show_box:
            os.remove(txt_name)

if __name__ == '__main__':

    tester = TestMSRATD500GWD(cfgs)
    tester.eval()

