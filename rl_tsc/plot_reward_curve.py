'''
Author: Maonan Wang
Date: 2025-04-23 11:28:32
Description: 绘制奖励曲线
LastEditors: WANG Maonan
LastEditTime: 2025-06-30 21:56:47
'''
from tshub.utils.plot_reward_curves import plot_reward_curve
from tshub.utils.get_abs_path import get_abs_path
path_convert = get_abs_path(__file__)

SCENARIO_NAME = "SouthKorea_Songdo"

if __name__ == '__main__':
    log_files = [
        path_convert(f'./results//{SCENARIO_NAME}/log/{i}.monitor.csv')
        for i in range(10)
    ]
    output_file = path_convert(f'./{SCENARIO_NAME}_reward.png')
    plot_reward_curve(log_files, output_file=output_file, window_size=2, fill_outliers=False)