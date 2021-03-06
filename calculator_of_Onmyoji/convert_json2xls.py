#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import os
import sys

from calculator_of_Onmyoji import load_data
from calculator_of_Onmyoji import write_data


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser()

parser.add_argument("-ESPS", "--effective-secondary-prop-show",
                    type=str2bool,
                    default=True,
                    help='是否展示副属性的有效条数，默认为True。如果不想展示输入False即可'
                         '"-ESPS True"为展示副属性有效条数'
                         '“输出类”为包含 攻击加成、速度、暴击、暴击伤害的有效条数'
                         '“奶盾类”为包含 生命加成、速度、暴击、暴击伤害的有效条数'
                         '“命中类”为包含 效果命中、速度的有效条数'
                         '“双堆类”为包含 效果命中、效果抵抗、速度的有效条数'
                         '首领御魂的固有属性也加入计算，首领御魂的满条为12分左右')


if __name__ == '__main__':
    args = parser.parse_args()
    esps_show = args.effective_secondary_prop_show
    print('Input args: %s' % args)
    json_files = load_data.get_ext_files('.json')

    if not json_files:
        print('There is no json file in current directory, exit.')
        sys.exit(1)

    for file_path in json_files:
        data = load_data.get_mitama_data_json(file_path, [])

        file_name, _ = os.path.splitext(file_path)
        file_name_xls = file_name + '.xls'
        
        if os.path.exists(file_name_xls):
            print('%s already exists, skip it.' % file_name_xls)
            continue

        write_data.write_original_mitama_data(file_name_xls, data, esps_show)

        print('File %s has been converted' % file_path)

    input('Press any key to exit')
