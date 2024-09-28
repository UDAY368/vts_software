from utils.json_ops import load_json_from_file
default_values_file_path = 'default_values\default_values.json'
# Read the Json File
stored_default_value_dict = load_json_from_file(default_values_file_path)
btc_excel_folder_path = "D:\\VTS_Software\\downloads\\auto_download_excels\\btc_excels"

if not stored_default_value_dict:
    pass
else:
    # Software folder path
    vts_software_folder_path = stored_default_value_dict["set_software_path"]
    output_excel_folder_path = stored_default_value_dict["output_excel_folder_path"]
    # cursor wait time
    wait_time_sec = stored_default_value_dict["wait_time_sec"]
    # calender x & y positions
    calender_1_tf = stored_default_value_dict["set_calender_x_y_position"][0]
    calender_2_tf = stored_default_value_dict["set_calender_x_y_position"][1]
    calender_5_tf = stored_default_value_dict["set_calender_x_y_position"][2]
    go_to_calender = stored_default_value_dict["set_calender_x_y_position"][3]
    choose_date = stored_default_value_dict["set_calender_x_y_position"][4]
    go_to_button = stored_default_value_dict["set_calender_x_y_position"][5]
    # chart x & y positions
    arrow_button = stored_default_value_dict["set_chart_x_y_positions"][0]
    export_chart = stored_default_value_dict["set_chart_x_y_positions"][1]
    chart_button = stored_default_value_dict["set_chart_x_y_positions"][2]
    one_TF_chart = stored_default_value_dict["set_chart_x_y_positions"][3]
    two_TF_chart = stored_default_value_dict["set_chart_x_y_positions"][4]
    five_TF_chart = stored_default_value_dict["set_chart_x_y_positions"][5]
    export_button = stored_default_value_dict["set_chart_x_y_positions"][6]
    # Auto Alert x & y positions
    initial_click = stored_default_value_dict["auto_alert_positions"][0]
    indicator_click = stored_default_value_dict["auto_alert_positions"][1]
    dots_click = stored_default_value_dict["auto_alert_positions"][2]
    add_alert = stored_default_value_dict["auto_alert_positions"][3]
    nh_create_button = stored_default_value_dict["auto_alert_positions"][4]
    click_condition = stored_default_value_dict["auto_alert_positions"][5]
    choose_low = stored_default_value_dict["auto_alert_positions"][6]
    nl_create_button = stored_default_value_dict["auto_alert_positions"][4]

layer_3_rank_1_col_weights = {
    "last_swing_per": 0.95,
    "last_swing_rand_per": -1,
    "last_swing_time": 0.9,
    "last_swing_rsi_dif": 0.86,
    "last_3_s_per_sum": 0.73,
    "last_3_s_per_avg": 0.73,
    "last_3_s_rand_sum": -0.77,
    "last_3_s_rand_avg": -0.77,
    "last_3_s_avg_time": 0.7,
    "last_3_s_rsi_diff_avg": 0.7,
    "all_swing_count": -0.44,
    "all_swings_pp_count": -0.44,
    "all_swings_np_count": -0.44,
    "all_swing_per_sum": 0.41,
    "all_swings_pp_sum": 0.41,
    "all_swings_np_sum": 0.41,
    "all_swings_pp_avg": 0.44,
    "all_swings_np_avg": 0.44,
    "all_swings_pp_med": 0.44,
    "all_swings_np_med": 0.44,
    "t_10_lrg_pp_sp_sum": 0.41,
    "t_10_lrg_np_sp_sum": 0.41,
    "t_10_lrg_pp_sp_avg": 0.44,
    "t_10_lrg_np_sp_avg": 0.44,
    "t_10_lrg_pp_sp_med": 0.44,
    "t_10_lrg_np_sp_med": 0.44,
    "t_10_sml_pp_sp_sum": 0.41,
    "t_10_sml_np_sp_sum": 0.41,
    "t_10_sml_pp_sp_avg": 0.44,
    "t_10_sml_np_sp_avg": 0.44,
    "t_10_sml_pp_sp_med": 0.44,
    "t_10_sml_np_sp_med": 0.44,
    "sp_pp_cnt_0_2_lst": -0.39,
    "sp_pp_cnt_2_4_lst": -0.39,
    "sp_pp_cnt_4_7_lst": 0.39,
    "sp_pp_cnt_7_15_lst": 0.39,
    "sp_pp_cnt_15_25_lst": 0.39,
    "sp_np_cnt_0_2_lst": -0.39,
    "sp_np_cnt_2_4_lst": -0.39,
    "sp_np_cnt_4_7_lst": 0.39,
    "sp_np_cnt_7_15_lst": 0.39,
    "sp_np_cnt_15_25_lst": 0.39,
    "all_swing_rand_per_sum": -0.48,
    "all_swings_rand_pp_sum": -0.48,
    "all_swings_rand_np_sum": -0.48,
    "all_swings_rand_pp_avg": -0.51,
    "all_swings_rand_np_avg": -0.51,
    "all_swings_rand_pp_med": -0.51,
    "all_swings_rand_np_med": -0.51,
    "t_10_lrg_pp_rand_sp_sum": -0.48,
    "t_10_lrg_np_rand_sp_sum": -0.48,
    "t_10_lrg_pp_rand_sp_avg": -0.51,
    "t_10_lrg_np_rand_sp_avg": -0.51,
    "t_10_lrg_pp_rand_sp_med": -0.51,
    "t_10_lrg_np_rand_sp_med": -0.51,
    "t_10_sml_pp_rand_sp_sum": -0.48,
    "t_10_sml_np_rand_sp_sum": -0.48,
    "t_10_sml_pp_rand_sp_avg": -0.51,
    "t_10_sml_np_rand_sp_avg": -0.51,
    "t_10_sml_pp_rand_sp_med": -0.51,
    "t_10_sml_np_rand_sp_med": -0.51,
    "all_swings_zero_rand_count": 0.63,
    "all_swings_zero_rand_pp_count": 0.63,
    "all_swings_zero_rand_np_count": 0.63,
    "all_swings_zero_rand_pp_sum": 0.6,
    "all_swings_zero_rand_np_sum": 0.6,
    "all_swing_zero_rand_per_sum": 0.6,
    "all_swings_zero_rand_pp_mean": 0.63,
    "all_swings_zero_rand_np_mean": 0.63,
    "all_swings_zero_rand_pp_med": 0.63,
    "all_swings_zero_rand_np_med": 0.63,
    "t_10_lrg_pp_zero_rand_sp_sum": 0.54,
    "t_10_lrg_np_zero_rand_sp_sum": 0.54,
    "t_10_lrg_pp_zero_rand_sp_avg": 0.57,
    "t_10_lrg_np_zero_rand_sp_avg": 0.57,
    "t_10_lrg_pp_zero_rand_sp_med": 0.57,
    "t_10_lrg_np_zero_rand_sp_med": 0.57,
    "t_10_sml_pp_zero_rand_sp_sum": 0.54,
    "t_10_sml_np_zero_rand_sp_sum": 0.54,
    "t_10_sml_pp_zero_rand_sp_avg": 0.57,
    "t_10_sml_np_zero_rand_sp_avg": 0.57,
    "t_10_sml_pp_zero_rand_sp_med": 0.57,
    "t_10_sml_np_zero_rand_sp_med": 0.57,
    "rand_pp_cnt_0_to_0_25_lst": 0.37,
    "rand_pp_cnt_0_25_to_0_5_lst": 0.37,
    "rand_pp_cnt_0_to_0_5_lst": 0.37,
    "rand_pp_cnt_0_5_to_1_lst": 0.37,
    "rand_pp_cnt_1_to_1_5_lst": 0.37,
    "rand_pp_cnt_0_5_to_1_5_lst": 0.37,
    "rand_pp_cnt_1_5_to_3_5_lst": -0.37,
    "rand_pp_cnt_3_5_to_7_lst": -0.37,
    "rand_pp_cnt_7_to_15_lst": -0.37,
    "rand_np_cnt_0_to_0_25_lst": 0.37,
    "rand_np_cnt_0_25_to_0_5_lst": 0.37,
    "rand_np_cnt_0_to_0_5_lst": 0.37,
    "rand_np_cnt_0_5_to_1_lst": 0.37,
    "rand_np_cnt_1_to_1_5_lst": 0.37,
    "rand_np_cnt_0_5_to_1_5_lst": 0.37,
    "rand_np_cnt_1_5_to_3_5_lst": -0.37,
    "rand_np_cnt_3_5_to_7_lst": -0.37,
    "rand_np_cnt_7_to_15_lst": -0.37,
    "all_swing_max_time": 0.34,
    "all_swing_avg_time": 0.34,
    "all_swing_median_time": 0.34,
    "pstv_swing_max_time": 0.34,
    "pstv_swing_avg_time": 0.34,
    "pstv_swing_median_time": 0.34,
    "neg_swing_max_time": 0.34,
    "neg_swing_avg_time": 0.34,
    "neg_swing_median_time": 0.34,
    "top_10_lrg_pstv_total_rand_per_change": 0.34,
    "top_10_lrg_pstv_max_time": 0.34,
    "top_10_lrg_pstv_avg_time": 0.34,
    "top_10_lrg_pstv_median_time": 0.34,
    "top_10_sml_pstv_total_rand_per_change": 0.34,
    "top_10_sml_pstv_max_time": 0.34,
    "top_10_sml_pstv_avg_time": 0.34,
    "top_10_sml_pstv_median_time": 0.34,
    "top_10_lrg_neg_total_rand_per_change": 0.34,
    "top_10_lrg_neg_max_time": 0.34,
    "top_10_lrg_neg_avg_time": 0.34,
    "top_10_lrg_neg_median_time": 0.34,
    "top_10_sml_neg_total_rand_per_change": 0.34,
    "top_10_sml_neg_max_time": 0.34,
    "top_10_sml_neg_avg_time": 0.34,
    "top_10_sml_neg_median_time": 0.34,
    "zero_rand_max_swings_time": 0.34,
    "zero_rand_avg_swings_time": 0.34,
    "zero_rand_med_swings_time": 0.34,
    "zero_rand_pstv_sp_max_swings_time": 0.34,
    "zero_rand_pstv_sp_avg_swings_time": 0.34,
    "zero_rand_pstv_sp_med_swings_time": 0.34,
    "zero_rand_neg_sp_max_swings_time": 0.34,
    "zero_rand_neg_sp_avg_swings_time": 0.34,
    "zero_rand_neg_sp_med_swings_time": 0.34,
    "all_swing_max_rsi_diff": 0.3,
    "all_swing_avg_rsi_diff": 0.3,
    "all_swing_median_rsi_diff": 0.3,
    "pstv_swing_max_rsi_diff": 0.3,
    "pstv_swing_avg_rsi_diff": 0.3,
    "pstv_swing_median_rsi_diff": 0.3,
    "neg_swing_max_rsi_diff": 0.3,
    "neg_swing_avg_rsi_diff": 0.3,
    "neg_swing_median_rsi_diff": 0.3,
    "top_10_lrg_pstv_max_rsi_diff": 0.3,
    "top_10_lrg_pstv_avg_rsi_diff": 0.3,
    "top_10_lrg_pstv_median_rsi_diff": 0.3,
    "top_10_sml_pstv_max_rsi_diff": 0.3,
    "top_10_sml_pstv_avg_rsi_diff": 0.3,
    "top_10_sml_pstv_median_rsi_diff": 0.3,
    "top_10_lrg_neg_max_rsi_diff": 0.3,
    "top_10_lrg_neg_avg_rsi_diff": 0.3,
    "top_10_lrg_neg_median_rsi_diff": 0.3,
    "top_10_sml_neg_max_rsi_diff": 0.3,
    "top_10_sml_neg_avg_rsi_diff": 0.3,
    "top_10_sml_neg_median_rsi_diff": 0.3,
    "zero_rand_max_swings_rsi_diff": 0.3,
    "zero_rand_avg_swings_rsi_diff": 0.3,
    "zero_rand_med_swings_rsi_diff": 0.3,
    "zero_rand_pstv_sp_max_swings_rsi_diff": 0.3,
    "zero_rand_pstv_sp_avg_swings_rsi_diff": 0.3,
    "zero_rand_pstv_sp_med_swings_rsi_diff": 0.3,
    "zero_rand_neg_sp_max_swings_rsi_diff": 0.3,
    "zero_rand_neg_sp_avg_swings_rsi_diff": 0.3,
    "zero_rand_neg_sp_med_swings_rsi_diff": 0.3,
    "total_fb": -0.27,
    "total_pstv_fb": -0.27,
    "total_neg_fb": -0.27
}

layer_3_rank_2_col_weights = {
    'last_swing_per': 0.95, 'last_swing_rand_per': -1, 'last_swing_time': 0.9, 'last_swing_rsi_dif': 0.86, 'last_3_s_per_sum': 0.73, 'last_3_s_rand_sum': -0.77, 'last_3_s_avg_time': 0.7, 'last_3_s_rsi_diff_avg': 0.7, 'all_swing_count': -0.44, 'all_swings_pp_count': -0.44, 'all_swings_np_count': -0.44, 'all_swing_per_sum': 0.41, 'all_swings_pp_sum': 0.41, 'all_swings_np_sum': 0.41, 't_10_lrg_pp_sp_sum': 0.41, 't_10_lrg_np_sp_sum': 0.41, 't_10_sml_pp_sp_sum': 0.41, 't_10_sml_np_sp_sum': 0.41, 'sp_pp_cnt_0_2_lst': -0.39, 'sp_pp_cnt_2_4_lst': -0.39, 'sp_pp_cnt_4_7_lst': 0.39, 'sp_pp_cnt_7_15_lst': 0.39, 'sp_pp_cnt_15_25_lst': 0.39, 'sp_np_cnt_0_2_lst': -0.39, 'sp_np_cnt_2_4_lst': -0.39, 'sp_np_cnt_4_7_lst': 0.39, 'sp_np_cnt_7_15_lst': 0.39, 'sp_np_cnt_15_25_lst': 0.39, 'all_swing_rand_per_sum': -0.48, 'all_swings_rand_pp_sum': -0.48, 'all_swings_rand_np_sum': -0.48, 't_10_lrg_pp_rand_sp_sum': -0.48, 't_10_lrg_np_rand_sp_sum': -0.48, 't_10_sml_pp_rand_sp_sum': -0.48, 't_10_sml_np_rand_sp_sum': -0.48, 'all_swings_zero_rand_count': 0.63, 'all_swings_zero_rand_pp_count': 0.63, 'all_swings_zero_rand_np_count': 0.63, 'all_swings_zero_rand_pp_sum': 0.6, 'all_swings_zero_rand_np_sum': 0.6, 'all_swing_zero_rand_per_sum': 0.6, 't_10_lrg_pp_zero_rand_sp_sum': 0.54, 't_10_lrg_np_zero_rand_sp_sum': 0.54, 't_10_sml_pp_zero_rand_sp_sum': 0.54, 't_10_sml_np_zero_rand_sp_sum': 0.54, 'rand_pp_cnt_0_to_0_25_lst': 0.37, 'rand_pp_cnt_0_25_to_0_5_lst': 0.37, 'rand_pp_cnt_0_to_0_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_lst': 0.37, 'rand_pp_cnt_1_to_1_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_5_lst': 0.37, 'rand_pp_cnt_1_5_to_3_5_lst': -0.37, 'rand_pp_cnt_3_5_to_7_lst': -0.37, 'rand_pp_cnt_7_to_15_lst': -0.37, 'rand_np_cnt_0_to_0_25_lst': 0.37, 'rand_np_cnt_0_25_to_0_5_lst': 0.37, 'rand_np_cnt_0_to_0_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_lst': 0.37, 'rand_np_cnt_1_to_1_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_5_lst': 0.37, 'rand_np_cnt_1_5_to_3_5_lst': -0.37, 'rand_np_cnt_3_5_to_7_lst': -0.37, 'rand_np_cnt_7_to_15_lst': -0.37, 'all_swing_avg_time': 0.34, 'pstv_swing_avg_time': 0.34, 'neg_swing_avg_time': 0.34, 'top_10_lrg_pstv_total_rand_per_change': 0.34, 'top_10_lrg_pstv_avg_time': 0.34, 'top_10_sml_pstv_total_rand_per_change': 0.34, 'top_10_sml_pstv_avg_time': 0.34, 'top_10_lrg_neg_avg_time': 0.34, 'top_10_sml_neg_avg_time': 0.34, 'zero_rand_avg_swings_time': 0.34, 'zero_rand_pstv_sp_avg_swings_time': 0.34, 'zero_rand_neg_sp_avg_swings_time': 0.34, 'all_swing_avg_rsi_diff': 0.3, 'pstv_swing_avg_rsi_diff': 0.3, 'neg_swing_avg_rsi_diff': 0.3, 'top_10_lrg_pstv_avg_rsi_diff': 0.3, 'top_10_sml_pstv_avg_rsi_diff': 0.3, 'top_10_lrg_neg_avg_rsi_diff': 0.3, 'top_10_sml_neg_avg_rsi_diff': 0.3, 'zero_rand_avg_swings_rsi_diff': 0.3, 'zero_rand_pstv_sp_avg_swings_rsi_diff': 0.3, 'zero_rand_neg_sp_avg_swings_rsi_diff': 0.3, 'total_fb': -0.27, 'total_pstv_fb': -0.27, 'total_neg_fb': -0.27}

layer_3_rank_3_col_weights = {
    'last_swing_per': 0.95, 'last_swing_rand_per': -1, 'last_swing_time': 0.9, 'last_swing_rsi_dif': 0.86, 'last_3_s_per_sum': 0.73, 'last_3_s_rand_avg': -0.77, 'last_3_s_avg_time': 0.7, 'last_3_s_rsi_diff_avg': 0.7, 'all_swing_count': -0.44, 'all_swings_pp_count': -0.44, 'all_swings_np_count': -0.44, 'all_swing_per_sum': 0.41, 'all_swings_pp_sum': 0.41, 'all_swings_np_sum': 0.41, 't_10_lrg_pp_sp_sum': 0.41, 't_10_lrg_np_sp_sum': 0.41, 't_10_sml_pp_sp_sum': 0.41, 't_10_sml_np_sp_sum': 0.41, 'sp_pp_cnt_0_2_lst': -0.39, 'sp_pp_cnt_2_4_lst': -0.39, 'sp_pp_cnt_4_7_lst': 0.39, 'sp_pp_cnt_7_15_lst': 0.39, 'sp_pp_cnt_15_25_lst': 0.39, 'sp_np_cnt_0_2_lst': -0.39, 'sp_np_cnt_2_4_lst': -0.39, 'sp_np_cnt_4_7_lst': 0.39, 'sp_np_cnt_7_15_lst': 0.39, 'sp_np_cnt_15_25_lst': 0.39, 'all_swings_rand_pp_avg': -0.51, 'all_swings_rand_np_avg': -0.51, 't_10_lrg_pp_rand_sp_avg': -0.51, 't_10_lrg_np_rand_sp_avg': -0.51, 't_10_sml_pp_rand_sp_avg': -0.51, 't_10_sml_np_rand_sp_avg': -0.51, 'all_swings_zero_rand_count': 0.63, 'all_swings_zero_rand_pp_count': 0.63, 'all_swings_zero_rand_np_count': 0.63, 'all_swings_zero_rand_pp_mean': 0.63, 'all_swings_zero_rand_np_mean': 0.63, 't_10_lrg_pp_zero_rand_sp_avg': 0.57, 't_10_lrg_np_zero_rand_sp_avg': 0.57, 't_10_sml_pp_zero_rand_sp_avg': 0.57, 't_10_sml_np_zero_rand_sp_avg': 0.57, 'rand_pp_cnt_0_to_0_25_lst': 0.37, 'rand_pp_cnt_0_25_to_0_5_lst': 0.37, 'rand_pp_cnt_0_to_0_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_lst': 0.37, 'rand_pp_cnt_1_to_1_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_5_lst': 0.37, 'rand_pp_cnt_1_5_to_3_5_lst': -0.37, 'rand_pp_cnt_3_5_to_7_lst': -0.37, 'rand_pp_cnt_7_to_15_lst': -0.37, 'rand_np_cnt_0_to_0_25_lst': 0.37, 'rand_np_cnt_0_25_to_0_5_lst': 0.37, 'rand_np_cnt_0_to_0_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_lst': 0.37, 'rand_np_cnt_1_to_1_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_5_lst': 0.37, 'rand_np_cnt_1_5_to_3_5_lst': -0.37, 'rand_np_cnt_3_5_to_7_lst': -0.37, 'rand_np_cnt_7_to_15_lst': -0.37, 'all_swing_avg_time': 0.34, 'pstv_swing_avg_time': 0.34, 'neg_swing_avg_time': 0.34, 'top_10_lrg_pstv_total_rand_per_change': 0.34, 'top_10_lrg_pstv_avg_time': 0.34, 'top_10_sml_pstv_total_rand_per_change': 0.34, 'top_10_sml_pstv_avg_time': 0.34, 'top_10_lrg_neg_avg_time': 0.34, 'top_10_sml_neg_avg_time': 0.34, 'zero_rand_avg_swings_time': 0.34, 'zero_rand_pstv_sp_avg_swings_time': 0.34, 'zero_rand_neg_sp_avg_swings_time': 0.34, 'all_swing_avg_rsi_diff': 0.3, 'pstv_swing_avg_rsi_diff': 0.3, 'neg_swing_avg_rsi_diff': 0.3, 'top_10_lrg_pstv_avg_rsi_diff': 0.3, 'top_10_sml_pstv_avg_rsi_diff': 0.3, 'top_10_lrg_neg_avg_rsi_diff': 0.3, 'top_10_sml_neg_avg_rsi_diff': 0.3, 'zero_rand_avg_swings_rsi_diff': 0.3, 'zero_rand_pstv_sp_avg_swings_rsi_diff': 0.3, 'zero_rand_neg_sp_avg_swings_rsi_diff': 0.3, 'total_fb': -0.27, 'total_pstv_fb': -0.27, 'total_neg_fb': -0.27}

layer_3_rank_4_col_weights = {
    'last_swing_per': 0.95, 'last_swing_rand_per': -1, 'last_swing_time': 0.9, 'last_swing_rsi_dif': 0.86, 'last_3_s_per_avg': 0.73, 'last_3_s_rand_avg': -0.77, 'last_3_s_avg_time': 0.7, 'last_3_s_rsi_diff_avg': 0.7, 'all_swing_count': -0.44, 'all_swings_pp_count': -0.44, 'all_swings_np_count': -0.44, 'all_swings_pp_avg': 0.44, 'all_swings_np_avg': 0.44, 't_10_lrg_pp_sp_avg': 0.44, 't_10_lrg_np_sp_avg': 0.44, 't_10_sml_pp_sp_avg': 0.44, 't_10_sml_np_sp_avg': 0.44, 'sp_pp_cnt_0_2_lst': -0.39, 'sp_pp_cnt_2_4_lst': -0.39, 'sp_pp_cnt_4_7_lst': 0.39, 'sp_pp_cnt_7_15_lst': 0.39, 'sp_pp_cnt_15_25_lst': 0.39, 'sp_np_cnt_0_2_lst': -0.39, 'sp_np_cnt_2_4_lst': -0.39, 'sp_np_cnt_4_7_lst': 0.39, 'sp_np_cnt_7_15_lst': 0.39, 'sp_np_cnt_15_25_lst': 0.39, 'all_swing_rand_per_sum': -0.48, 'all_swings_rand_pp_sum': -0.48, 'all_swings_rand_np_sum': -0.48, 't_10_lrg_pp_rand_sp_sum': -0.48, 't_10_lrg_np_rand_sp_sum': -0.48, 't_10_sml_pp_rand_sp_sum': -0.48, 't_10_sml_np_rand_sp_sum': -0.48, 'all_swings_zero_rand_count': 0.63, 'all_swings_zero_rand_pp_count': 0.63, 'all_swings_zero_rand_np_count': 0.63, 'all_swings_zero_rand_pp_sum': 0.6, 'all_swings_zero_rand_np_sum': 0.6, 'all_swing_zero_rand_per_sum': 0.6, 't_10_lrg_pp_zero_rand_sp_sum': 0.54, 't_10_lrg_np_zero_rand_sp_sum': 0.54, 't_10_sml_pp_zero_rand_sp_sum': 0.54, 't_10_sml_np_zero_rand_sp_sum': 0.54, 'rand_pp_cnt_0_to_0_25_lst': 0.37, 'rand_pp_cnt_0_25_to_0_5_lst': 0.37, 'rand_pp_cnt_0_to_0_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_lst': 0.37, 'rand_pp_cnt_1_to_1_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_5_lst': 0.37, 'rand_pp_cnt_1_5_to_3_5_lst': -0.37, 'rand_pp_cnt_3_5_to_7_lst': -0.37, 'rand_pp_cnt_7_to_15_lst': -0.37, 'rand_np_cnt_0_to_0_25_lst': 0.37, 'rand_np_cnt_0_25_to_0_5_lst': 0.37, 'rand_np_cnt_0_to_0_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_lst': 0.37, 'rand_np_cnt_1_to_1_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_5_lst': 0.37, 'rand_np_cnt_1_5_to_3_5_lst': -0.37, 'rand_np_cnt_3_5_to_7_lst': -0.37, 'rand_np_cnt_7_to_15_lst': -0.37, 'all_swing_avg_time': 0.34, 'pstv_swing_avg_time': 0.34, 'neg_swing_avg_time': 0.34, 'top_10_lrg_pstv_total_rand_per_change': 0.34, 'top_10_lrg_pstv_avg_time': 0.34, 'top_10_sml_pstv_total_rand_per_change': 0.34, 'top_10_sml_pstv_avg_time': 0.34, 'top_10_lrg_neg_avg_time': 0.34, 'top_10_sml_neg_avg_time': 0.34, 'zero_rand_avg_swings_time': 0.34, 'zero_rand_pstv_sp_avg_swings_time': 0.34, 'zero_rand_neg_sp_avg_swings_time': 0.34, 'all_swing_avg_rsi_diff': 0.3, 'pstv_swing_avg_rsi_diff': 0.3, 'neg_swing_avg_rsi_diff': 0.3, 'top_10_lrg_pstv_avg_rsi_diff': 0.3, 'top_10_sml_pstv_avg_rsi_diff': 0.3, 'top_10_lrg_neg_avg_rsi_diff': 0.3, 'top_10_sml_neg_avg_rsi_diff': 0.3, 'zero_rand_avg_swings_rsi_diff': 0.3, 'zero_rand_neg_sp_avg_swings_rsi_diff': 0.3, 'total_fb': -0.27, 'total_pstv_fb': -0.27, 'total_neg_fb': -0.27}

layer_3_rank_5_col_weights = {
    'last_swing_per': 0.95, 'last_swing_rand_per': -1, 'last_swing_time': 0.9, 'last_swing_rsi_dif': 0.86, 'last_3_s_per_avg': 0.73, 'last_3_s_rand_avg': -0.77, 'last_3_s_avg_time': 0.7, 'last_3_s_rsi_diff_avg': 0.7, 'all_swing_count': -0.44, 'all_swings_pp_count': -0.44, 'all_swings_np_count': -0.44, 'all_swings_pp_avg': 0.44, 'all_swings_np_avg': 0.44, 't_10_lrg_pp_sp_avg': 0.44, 't_10_lrg_np_sp_avg': 0.44, 't_10_sml_pp_sp_avg': 0.44, 't_10_sml_np_sp_avg': 0.44, 'sp_pp_cnt_0_2_lst': -0.39, 'sp_pp_cnt_2_4_lst': -0.39, 'sp_pp_cnt_4_7_lst': 0.39, 'sp_pp_cnt_7_15_lst': 0.39, 'sp_pp_cnt_15_25_lst': 0.39, 'sp_np_cnt_0_2_lst': -0.39, 'sp_np_cnt_2_4_lst': -0.39, 'sp_np_cnt_4_7_lst': 0.39, 'sp_np_cnt_7_15_lst': 0.39, 'sp_np_cnt_15_25_lst': 0.39, 'all_swings_rand_pp_avg': -0.51, 'all_swings_rand_np_avg': -0.51, 't_10_lrg_pp_rand_sp_avg': -0.51, 't_10_lrg_np_rand_sp_avg': -0.51, 't_10_sml_pp_rand_sp_avg': -0.51, 't_10_sml_np_rand_sp_avg': -0.51, 'all_swings_zero_rand_count': 0.63, 'all_swings_zero_rand_pp_count': 0.63, 'all_swings_zero_rand_np_count': 0.63, 'all_swings_zero_rand_pp_mean': 0.63, 'all_swings_zero_rand_np_mean': 0.63, 't_10_lrg_pp_zero_rand_sp_avg': 0.57, 't_10_lrg_np_zero_rand_sp_avg': 0.57, 't_10_sml_pp_zero_rand_sp_avg': 0.57, 't_10_sml_np_zero_rand_sp_avg': 0.57, 'rand_pp_cnt_0_to_0_25_lst': 0.37, 'rand_pp_cnt_0_25_to_0_5_lst': 0.37, 'rand_pp_cnt_0_to_0_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_lst': 0.37, 'rand_pp_cnt_1_to_1_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_5_lst': 0.37, 'rand_pp_cnt_1_5_to_3_5_lst': -0.37, 'rand_pp_cnt_3_5_to_7_lst': -0.37, 'rand_pp_cnt_7_to_15_lst': -0.37, 'rand_np_cnt_0_to_0_25_lst': 0.37, 'rand_np_cnt_0_25_to_0_5_lst': 0.37, 'rand_np_cnt_0_to_0_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_lst': 0.37, 'rand_np_cnt_1_to_1_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_5_lst': 0.37, 'rand_np_cnt_1_5_to_3_5_lst': -0.37, 'rand_np_cnt_3_5_to_7_lst': -0.37, 'rand_np_cnt_7_to_15_lst': -0.37, 'all_swing_avg_time': 0.34, 'pstv_swing_avg_time': 0.34, 'neg_swing_avg_time': 0.34, 'top_10_lrg_pstv_total_rand_per_change': 0.34, 'top_10_lrg_pstv_avg_time': 0.34, 'top_10_sml_pstv_total_rand_per_change': 0.34, 'top_10_sml_pstv_avg_time': 0.34, 'top_10_lrg_neg_avg_time': 0.34, 'top_10_sml_neg_avg_time': 0.34, 'zero_rand_avg_swings_time': 0.34, 'zero_rand_pstv_sp_avg_swings_time': 0.34, 'zero_rand_neg_sp_avg_swings_time': 0.34, 'all_swing_avg_rsi_diff': 0.3, 'pstv_swing_avg_rsi_diff': 0.3, 'neg_swing_avg_rsi_diff': 0.3, 'top_10_lrg_pstv_avg_rsi_diff': 0.3, 'top_10_sml_pstv_avg_rsi_diff': 0.3, 'top_10_lrg_neg_avg_rsi_diff': 0.3, 'top_10_sml_neg_avg_rsi_diff': 0.3, 'zero_rand_avg_swings_rsi_diff': 0.3, 'zero_rand_neg_sp_avg_swings_rsi_diff': 0.3, 'total_fb': -0.27, 'total_pstv_fb': -0.27, 'total_neg_fb': -0.27}

layer_3_rank_6_col_weights = {
    'last_swing_per': 0.95, 'last_swing_rand_per': -1, 'last_swing_time': 0.9, 'last_swing_rsi_dif': 0.86, 'last_3_s_per_avg': 0.73, 'last_3_s_rand_avg': -0.77, 'last_3_s_avg_time': 0.7, 'last_3_s_rsi_diff_avg': 0.7, 'all_swing_count': -0.44, 'all_swings_pp_count': -0.44, 'all_swings_np_count': -0.44, 'all_swings_pp_med': 0.44, 'all_swings_np_med': 0.44, 't_10_lrg_pp_sp_med': 0.44, 't_10_lrg_np_sp_med': 0.44, 't_10_sml_pp_sp_med': 0.44, 't_10_sml_np_sp_med': 0.44, 'sp_pp_cnt_0_2_lst': -0.39, 'sp_pp_cnt_2_4_lst': -0.39, 'sp_pp_cnt_4_7_lst': 0.39, 'sp_pp_cnt_7_15_lst': 0.39, 'sp_pp_cnt_15_25_lst': 0.39, 'sp_np_cnt_0_2_lst': -0.39, 'sp_np_cnt_2_4_lst': -0.39, 'sp_np_cnt_4_7_lst': 0.39, 'sp_np_cnt_7_15_lst': 0.39, 'sp_np_cnt_15_25_lst': 0.39, 'all_swings_rand_pp_med': -0.51, 'all_swings_rand_np_med': -0.51, 't_10_lrg_pp_rand_sp_med': -0.51, 't_10_lrg_np_rand_sp_med': -0.51, 't_10_sml_pp_rand_sp_med': -0.51, 't_10_sml_np_rand_sp_med': -0.51, 'all_swings_zero_rand_count': 0.63, 'all_swings_zero_rand_pp_count': 0.63, 'all_swings_zero_rand_np_count': 0.63, 'all_swings_zero_rand_pp_med': 0.63, 'all_swings_zero_rand_np_med': 0.63, 't_10_lrg_pp_zero_rand_sp_med': 0.57, 't_10_lrg_np_zero_rand_sp_med': 0.57, 't_10_sml_pp_zero_rand_sp_med': 0.57, 't_10_sml_np_zero_rand_sp_med': 0.57, 'rand_pp_cnt_0_to_0_25_lst': 0.37, 'rand_pp_cnt_0_25_to_0_5_lst': 0.37, 'rand_pp_cnt_0_to_0_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_lst': 0.37, 'rand_pp_cnt_1_to_1_5_lst': 0.37, 'rand_pp_cnt_0_5_to_1_5_lst': 0.37, 'rand_pp_cnt_1_5_to_3_5_lst': -0.37, 'rand_pp_cnt_3_5_to_7_lst': -0.37, 'rand_pp_cnt_7_to_15_lst': -0.37, 'rand_np_cnt_0_to_0_25_lst': 0.37, 'rand_np_cnt_0_25_to_0_5_lst': 0.37, 'rand_np_cnt_0_to_0_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_lst': 0.37, 'rand_np_cnt_1_to_1_5_lst': 0.37, 'rand_np_cnt_0_5_to_1_5_lst': 0.37, 'rand_np_cnt_1_5_to_3_5_lst': -0.37, 'rand_np_cnt_3_5_to_7_lst': -0.37, 'rand_np_cnt_7_to_15_lst': -0.37, 'all_swing_median_time': 0.34, 'pstv_swing_median_time': 0.34, 'neg_swing_median_time': 0.34, 'top_10_lrg_pstv_total_rand_per_change': 0.34, 'top_10_lrg_pstv_median_time': 0.34, 'top_10_sml_pstv_total_rand_per_change': 0.34, 'top_10_sml_pstv_median_time': 0.34, 'top_10_lrg_neg_median_time': 0.34, 'top_10_sml_neg_median_time': 0.34, 'zero_rand_med_swings_time': 0.34, 'zero_rand_pstv_sp_med_swings_time': 0.34, 'zero_rand_neg_sp_med_swings_time': 0.34, 'all_swing_median_rsi_diff': 0.3, 'pstv_swing_median_rsi_diff': 0.3, 'neg_swing_median_rsi_diff': 0.3, 'top_10_sml_pstv_median_rsi_diff': 0.3, 'top_10_lrg_neg_median_rsi_diff': 0.3, 'top_10_sml_neg_median_rsi_diff': 0.3, 'zero_rand_med_swings_rsi_diff': 0.3, 'zero_rand_pstv_sp_med_swings_rsi_diff': 0.3, 'zero_rand_neg_sp_med_swings_rsi_diff': 0.3, 'total_fb': -0.27, 'total_pstv_fb': -0.27, 'total_neg_fb': -0.27}

layer_3_str_info_col_names = [
    'coin_name', 'coin_time_tf', 'swing_1_info', 'swing_2_info', 'swing_3_info', 'swing_1_dir', 'swing_2_dir', 'swing_3_dir', 't_5_lrg_pp_sp_lst', 't_5_lrg_np_sp_lst', 't_3_sp_pp_ranges', 't_3_sp_np_ranges', 't_5_lrg_pp_rand_sp_lst', 't_5_lrg_np_rand_sp_lst', 't_5_lrg_pp_zero_rand_sp_lst', 't_5_lrg_np_zero_rand_sp_lst', 't_3_rand_pp_ranges', 't_3_rand_np_ranges', 'last_fb_time']

layer_3_rank_1_col_names = [
    "coin_name","coin_time_tf","last_swing_per","last_swing_rand_per","last_swing_time","last_swing_rsi_dif","last_3_s_per_sum","last_3_s_per_avg","last_3_s_rand_sum","last_3_s_rand_avg","last_3_s_avg_time","last_3_s_rsi_diff_avg","all_swing_count","all_swings_pp_count","all_swings_np_count","all_swing_per_sum","all_swings_pp_sum","all_swings_np_sum","all_swings_pp_avg","all_swings_np_avg","all_swings_pp_med","all_swings_np_med","t_10_lrg_pp_sp_sum","t_10_lrg_np_sp_sum","t_10_lrg_pp_sp_avg","t_10_lrg_np_sp_avg","t_10_lrg_pp_sp_med","t_10_lrg_np_sp_med","t_10_sml_pp_sp_sum","t_10_sml_np_sp_sum","t_10_sml_pp_sp_avg","t_10_sml_np_sp_avg","t_10_sml_pp_sp_med","t_10_sml_np_sp_med","sp_pp_cnt_0_2_lst","sp_pp_cnt_2_4_lst","sp_pp_cnt_4_7_lst","sp_pp_cnt_7_15_lst","sp_pp_cnt_15_25_lst","sp_np_cnt_0_2_lst","sp_np_cnt_2_4_lst","sp_np_cnt_4_7_lst","sp_np_cnt_7_15_lst","sp_np_cnt_15_25_lst","all_swing_rand_per_sum","all_swings_rand_pp_sum","all_swings_rand_np_sum","all_swings_rand_pp_avg","all_swings_rand_np_avg","all_swings_rand_pp_med","all_swings_rand_np_med","t_10_lrg_pp_rand_sp_sum","t_10_lrg_np_rand_sp_sum","t_10_lrg_pp_rand_sp_avg","t_10_lrg_np_rand_sp_avg","t_10_lrg_pp_rand_sp_med","t_10_lrg_np_rand_sp_med","t_10_sml_pp_rand_sp_sum","t_10_sml_np_rand_sp_sum","t_10_sml_pp_rand_sp_avg","t_10_sml_np_rand_sp_avg","t_10_sml_pp_rand_sp_med","t_10_sml_np_rand_sp_med","all_swings_zero_rand_count","all_swings_zero_rand_pp_count","all_swings_zero_rand_np_count","all_swings_zero_rand_pp_sum","all_swings_zero_rand_np_sum","all_swing_zero_rand_per_sum","all_swings_zero_rand_pp_mean","all_swings_zero_rand_np_mean","all_swings_zero_rand_pp_med","all_swings_zero_rand_np_med","t_10_lrg_pp_zero_rand_sp_sum","t_10_lrg_np_zero_rand_sp_sum","t_10_lrg_pp_zero_rand_sp_avg","t_10_lrg_np_zero_rand_sp_avg","t_10_lrg_pp_zero_rand_sp_med","t_10_lrg_np_zero_rand_sp_med","t_10_sml_pp_zero_rand_sp_sum","t_10_sml_np_zero_rand_sp_sum","t_10_sml_pp_zero_rand_sp_avg","t_10_sml_np_zero_rand_sp_avg","t_10_sml_pp_zero_rand_sp_med","t_10_sml_np_zero_rand_sp_med","rand_pp_cnt_0_to_0_25_lst","rand_pp_cnt_0_25_to_0_5_lst","rand_pp_cnt_0_to_0_5_lst","rand_pp_cnt_0_5_to_1_lst","rand_pp_cnt_1_to_1_5_lst","rand_pp_cnt_0_5_to_1_5_lst","rand_pp_cnt_1_5_to_3_5_lst","rand_pp_cnt_3_5_to_7_lst","rand_pp_cnt_7_to_15_lst","rand_np_cnt_0_to_0_25_lst","rand_np_cnt_0_25_to_0_5_lst","rand_np_cnt_0_to_0_5_lst","rand_np_cnt_0_5_to_1_lst","rand_np_cnt_1_to_1_5_lst","rand_np_cnt_0_5_to_1_5_lst","rand_np_cnt_1_5_to_3_5_lst","rand_np_cnt_3_5_to_7_lst","rand_np_cnt_7_to_15_lst","all_swing_max_time","all_swing_avg_time","all_swing_median_time","pstv_swing_max_time","pstv_swing_avg_time","pstv_swing_median_time","neg_swing_max_time","neg_swing_avg_time","neg_swing_median_time","top_10_lrg_pstv_total_rand_per_change","top_10_lrg_pstv_max_time","top_10_lrg_pstv_avg_time","top_10_lrg_pstv_median_time","top_10_sml_pstv_total_rand_per_change","top_10_sml_pstv_max_time","top_10_sml_pstv_avg_time","top_10_sml_pstv_median_time","top_10_lrg_neg_total_rand_per_change","top_10_lrg_neg_max_time","top_10_lrg_neg_avg_time","top_10_lrg_neg_median_time","top_10_sml_neg_total_rand_per_change","top_10_sml_neg_max_time","top_10_sml_neg_avg_time","top_10_sml_neg_median_time","zero_rand_max_swings_time","zero_rand_avg_swings_time","zero_rand_med_swings_time","zero_rand_pstv_sp_max_swings_time","zero_rand_pstv_sp_avg_swings_time","zero_rand_pstv_sp_med_swings_time","zero_rand_neg_sp_max_swings_time","zero_rand_neg_sp_avg_swings_time","zero_rand_neg_sp_med_swings_time","all_swing_max_rsi_diff","all_swing_avg_rsi_diff","all_swing_median_rsi_diff","pstv_swing_max_rsi_diff","pstv_swing_avg_rsi_diff","pstv_swing_median_rsi_diff","neg_swing_max_rsi_diff","neg_swing_avg_rsi_diff","neg_swing_median_rsi_diff","top_10_lrg_pstv_max_rsi_diff","top_10_lrg_pstv_avg_rsi_diff","top_10_lrg_pstv_median_rsi_diff","top_10_sml_pstv_max_rsi_diff","top_10_sml_pstv_avg_rsi_diff","top_10_sml_pstv_median_rsi_diff","top_10_lrg_neg_max_rsi_diff","top_10_lrg_neg_avg_rsi_diff","top_10_lrg_neg_median_rsi_diff","top_10_sml_neg_max_rsi_diff","top_10_sml_neg_avg_rsi_diff","top_10_sml_neg_median_rsi_diff","zero_rand_max_swings_rsi_diff","zero_rand_avg_swings_rsi_diff","zero_rand_med_swings_rsi_diff","zero_rand_pstv_sp_max_swings_rsi_diff","zero_rand_pstv_sp_avg_swings_rsi_diff","zero_rand_pstv_sp_med_swings_rsi_diff","zero_rand_neg_sp_max_swings_rsi_diff","zero_rand_neg_sp_avg_swings_rsi_diff","zero_rand_neg_sp_med_swings_rsi_diff","total_fb","total_pstv_fb","total_neg_fb"] 

layer_3_rank_2_col_names = [
    "coin_name", "coin_time_tf", "last_swing_per", "last_swing_rand_per", "last_swing_time",
    "last_swing_rsi_dif", "last_3_s_per_sum", "last_3_s_rand_sum", "last_3_s_avg_time",
    "last_3_s_rsi_diff_avg", "all_swing_count", "all_swings_pp_count", "all_swings_np_count",
    "all_swing_per_sum", "all_swings_pp_sum", "all_swings_np_sum", "t_10_lrg_pp_sp_sum",
    "t_10_lrg_np_sp_sum", "t_10_sml_pp_sp_sum", "t_10_sml_np_sp_sum", "sp_pp_cnt_0_2_lst",
    "sp_pp_cnt_2_4_lst", "sp_pp_cnt_4_7_lst", "sp_pp_cnt_7_15_lst", "sp_pp_cnt_15_25_lst",
    "sp_np_cnt_0_2_lst", "sp_np_cnt_2_4_lst", "sp_np_cnt_4_7_lst", "sp_np_cnt_7_15_lst",
    "sp_np_cnt_15_25_lst", "all_swing_rand_per_sum", "all_swings_rand_pp_sum",
    "all_swings_rand_np_sum", "t_10_lrg_pp_rand_sp_sum", "t_10_lrg_np_rand_sp_sum",
    "t_10_sml_pp_rand_sp_sum", "t_10_sml_np_rand_sp_sum", "all_swings_zero_rand_count",
    "all_swings_zero_rand_pp_count", "all_swings_zero_rand_np_count",
    "all_swings_zero_rand_pp_sum", "all_swings_zero_rand_np_sum", "all_swing_zero_rand_per_sum",
    "t_10_lrg_pp_zero_rand_sp_sum", "t_10_lrg_np_zero_rand_sp_sum",
    "t_10_sml_pp_zero_rand_sp_sum", "t_10_sml_np_zero_rand_sp_sum", "rand_pp_cnt_0_to_0_25_lst",
    "rand_pp_cnt_0_25_to_0_5_lst", "rand_pp_cnt_0_to_0_5_lst", "rand_pp_cnt_0_5_to_1_lst",
    "rand_pp_cnt_1_to_1_5_lst", "rand_pp_cnt_0_5_to_1_5_lst", "rand_pp_cnt_1_5_to_3_5_lst",
    "rand_pp_cnt_3_5_to_7_lst", "rand_pp_cnt_7_to_15_lst", "rand_np_cnt_0_to_0_25_lst",
    "rand_np_cnt_0_25_to_0_5_lst", "rand_np_cnt_0_to_0_5_lst", "rand_np_cnt_0_5_to_1_lst",
    "rand_np_cnt_1_to_1_5_lst", "rand_np_cnt_0_5_to_1_5_lst", "rand_np_cnt_1_5_to_3_5_lst",
    "rand_np_cnt_3_5_to_7_lst", "rand_np_cnt_7_to_15_lst", "all_swing_avg_time",
    "pstv_swing_avg_time", "neg_swing_avg_time", "top_10_lrg_pstv_total_rand_per_change",
    "top_10_lrg_pstv_avg_time", "top_10_sml_pstv_total_rand_per_change", "top_10_sml_pstv_avg_time",
    "top_10_lrg_neg_avg_time", "top_10_sml_neg_avg_time", "zero_rand_avg_swings_time",
    "zero_rand_pstv_sp_avg_swings_time", "zero_rand_neg_sp_avg_swings_time", "all_swing_avg_rsi_diff",
    "pstv_swing_avg_rsi_diff", "neg_swing_avg_rsi_diff", "top_10_lrg_pstv_avg_rsi_diff",
    "top_10_sml_pstv_avg_rsi_diff", "top_10_lrg_neg_avg_rsi_diff", "top_10_sml_neg_avg_rsi_diff",
    "zero_rand_avg_swings_rsi_diff", "zero_rand_pstv_sp_avg_swings_rsi_diff",
    "zero_rand_neg_sp_avg_swings_rsi_diff", "total_fb", "total_pstv_fb", "total_neg_fb"
]

layer_3_rank_3_col_names = [
    "coin_name", "coin_time_tf", "last_swing_per", "last_swing_rand_per", "last_swing_time",
    "last_swing_rsi_dif", "last_3_s_per_sum", "last_3_s_rand_avg", "last_3_s_avg_time",
    "last_3_s_rsi_diff_avg", "all_swing_count", "all_swings_pp_count", "all_swings_np_count",
    "all_swing_per_sum", "all_swings_pp_sum", "all_swings_np_sum", "t_10_lrg_pp_sp_sum",
    "t_10_lrg_np_sp_sum", "t_10_sml_pp_sp_sum", "t_10_sml_np_sp_sum", "sp_pp_cnt_0_2_lst",
    "sp_pp_cnt_2_4_lst", "sp_pp_cnt_4_7_lst", "sp_pp_cnt_7_15_lst", "sp_pp_cnt_15_25_lst",
    "sp_np_cnt_0_2_lst", "sp_np_cnt_2_4_lst", "sp_np_cnt_4_7_lst", "sp_np_cnt_7_15_lst",
    "sp_np_cnt_15_25_lst", "all_swings_rand_pp_avg", "all_swings_rand_np_avg",
    "t_10_lrg_pp_rand_sp_avg", "t_10_lrg_np_rand_sp_avg", "t_10_sml_pp_rand_sp_avg",
    "t_10_sml_np_rand_sp_avg", "all_swings_zero_rand_count", "all_swings_zero_rand_pp_count",
    "all_swings_zero_rand_np_count", "all_swings_zero_rand_pp_mean", "all_swings_zero_rand_np_mean",
    "t_10_lrg_pp_zero_rand_sp_avg", "t_10_lrg_np_zero_rand_sp_avg",
    "t_10_sml_pp_zero_rand_sp_avg", "t_10_sml_np_zero_rand_sp_avg", "rand_pp_cnt_0_to_0_25_lst",
    "rand_pp_cnt_0_25_to_0_5_lst", "rand_pp_cnt_0_to_0_5_lst", "rand_pp_cnt_0_5_to_1_lst",
    "rand_pp_cnt_1_to_1_5_lst", "rand_pp_cnt_0_5_to_1_5_lst", "rand_pp_cnt_1_5_to_3_5_lst",
    "rand_pp_cnt_3_5_to_7_lst", "rand_pp_cnt_7_to_15_lst", "rand_np_cnt_0_to_0_25_lst",
    "rand_np_cnt_0_25_to_0_5_lst", "rand_np_cnt_0_to_0_5_lst", "rand_np_cnt_0_5_to_1_lst",
    "rand_np_cnt_1_to_1_5_lst", "rand_np_cnt_0_5_to_1_5_lst", "rand_np_cnt_1_5_to_3_5_lst",
    "rand_np_cnt_3_5_to_7_lst", "rand_np_cnt_7_to_15_lst", "all_swing_avg_time",
    "pstv_swing_avg_time", "neg_swing_avg_time", "top_10_lrg_pstv_total_rand_per_change",
    "top_10_lrg_pstv_avg_time", "top_10_sml_pstv_total_rand_per_change", "top_10_sml_pstv_avg_time",
    "top_10_lrg_neg_avg_time", "top_10_sml_neg_avg_time", "zero_rand_avg_swings_time",
    "zero_rand_pstv_sp_avg_swings_time", "zero_rand_neg_sp_avg_swings_time", "all_swing_avg_rsi_diff",
    "pstv_swing_avg_rsi_diff", "neg_swing_avg_rsi_diff", "top_10_lrg_pstv_avg_rsi_diff",
    "top_10_sml_pstv_avg_rsi_diff", "top_10_lrg_neg_avg_rsi_diff", "top_10_sml_neg_avg_rsi_diff",
    "zero_rand_avg_swings_rsi_diff", "zero_rand_pstv_sp_avg_swings_rsi_diff",
    "zero_rand_neg_sp_avg_swings_rsi_diff", "total_fb", "total_pstv_fb", "total_neg_fb"
]

layer_3_rank_4_col_names = [
    "coin_name","coin_time_tf","last_swing_per","last_swing_rand_per","last_swing_time","last_swing_rsi_dif","last_3_s_per_avg","last_3_s_rand_avg","last_3_s_avg_time","last_3_s_rsi_diff_avg","all_swing_count","all_swings_pp_count","all_swings_np_count","all_swings_pp_avg","all_swings_np_avg","t_10_lrg_pp_sp_avg","t_10_lrg_np_sp_avg","t_10_sml_pp_sp_avg","t_10_sml_np_sp_avg","sp_pp_cnt_0_2_lst","sp_pp_cnt_2_4_lst","sp_pp_cnt_4_7_lst","sp_pp_cnt_7_15_lst","sp_pp_cnt_15_25_lst","sp_np_cnt_0_2_lst","sp_np_cnt_2_4_lst","sp_np_cnt_4_7_lst","sp_np_cnt_7_15_lst","sp_np_cnt_15_25_lst","all_swing_rand_per_sum","all_swings_rand_pp_sum","all_swings_rand_np_sum","t_10_lrg_pp_rand_sp_sum","t_10_lrg_np_rand_sp_sum","t_10_sml_pp_rand_sp_sum","t_10_sml_np_rand_sp_sum","all_swings_zero_rand_count","all_swings_zero_rand_pp_count","all_swings_zero_rand_np_count","all_swings_zero_rand_pp_sum","all_swings_zero_rand_np_sum","all_swing_zero_rand_per_sum","t_10_lrg_pp_zero_rand_sp_sum","t_10_lrg_np_zero_rand_sp_sum","t_10_sml_pp_zero_rand_sp_sum","t_10_sml_np_zero_rand_sp_sum","rand_pp_cnt_0_to_0_25_lst","rand_pp_cnt_0_25_to_0_5_lst","rand_pp_cnt_0_to_0_5_lst","rand_pp_cnt_0_5_to_1_lst","rand_pp_cnt_1_to_1_5_lst","rand_pp_cnt_0_5_to_1_5_lst","rand_pp_cnt_1_5_to_3_5_lst","rand_pp_cnt_3_5_to_7_lst","rand_pp_cnt_7_to_15_lst","rand_np_cnt_0_to_0_25_lst","rand_np_cnt_0_25_to_0_5_lst","rand_np_cnt_0_to_0_5_lst","rand_np_cnt_0_5_to_1_lst","rand_np_cnt_1_to_1_5_lst","rand_np_cnt_0_5_to_1_5_lst","rand_np_cnt_1_5_to_3_5_lst","rand_np_cnt_3_5_to_7_lst","rand_np_cnt_7_to_15_lst","all_swing_avg_time","pstv_swing_avg_time","neg_swing_avg_time","top_10_lrg_pstv_total_rand_per_change","top_10_lrg_pstv_avg_time","top_10_sml_pstv_total_rand_per_change","top_10_sml_pstv_avg_time","top_10_lrg_neg_avg_time","top_10_sml_neg_avg_time","zero_rand_avg_swings_time","zero_rand_pstv_sp_avg_swings_time","zero_rand_neg_sp_avg_swings_time","all_swing_avg_rsi_diff","pstv_swing_avg_rsi_diff","neg_swing_avg_rsi_diff","top_10_lrg_pstv_avg_rsi_diff","top_10_sml_pstv_avg_rsi_diff","top_10_lrg_neg_avg_rsi_diff","top_10_sml_neg_avg_rsi_diff","zero_rand_avg_swings_rsi_diff","zero_rand_pstv_sp_avg_rsi_diff","zero_rand_neg_sp_avg_swings_rsi_diff","total_fb","total_pstv_fb","total_neg_fb"
]

layer_3_rank_5_col_names = [
    "coin_name","coin_time_tf","last_swing_per","last_swing_rand_per","last_swing_time","last_swing_rsi_dif","last_3_s_per_avg","last_3_s_rand_avg","last_3_s_avg_time","last_3_s_rsi_diff_avg","all_swing_count","all_swings_pp_count","all_swings_np_count","all_swings_pp_avg","all_swings_np_avg","t_10_lrg_pp_sp_avg","t_10_lrg_np_sp_avg","t_10_sml_pp_sp_avg","t_10_sml_np_sp_avg","sp_pp_cnt_0_2_lst","sp_pp_cnt_2_4_lst","sp_pp_cnt_4_7_lst","sp_pp_cnt_7_15_lst","sp_pp_cnt_15_25_lst","sp_np_cnt_0_2_lst","sp_np_cnt_2_4_lst","sp_np_cnt_4_7_lst","sp_np_cnt_7_15_lst","sp_np_cnt_15_25_lst","all_swings_rand_pp_avg","all_swings_rand_np_avg","t_10_lrg_pp_rand_sp_avg","t_10_lrg_np_rand_sp_avg","t_10_sml_pp_rand_sp_avg","t_10_sml_np_rand_sp_avg","all_swings_zero_rand_count","all_swings_zero_rand_pp_count","all_swings_zero_rand_np_count","all_swings_zero_rand_pp_mean","all_swings_zero_rand_np_mean","t_10_lrg_pp_zero_rand_sp_avg","t_10_lrg_np_zero_rand_sp_avg","t_10_sml_pp_zero_rand_sp_avg","t_10_sml_np_zero_rand_sp_avg","rand_pp_cnt_0_to_0_25_lst","rand_pp_cnt_0_25_to_0_5_lst","rand_pp_cnt_0_to_0_5_lst","rand_pp_cnt_0_5_to_1_lst","rand_pp_cnt_1_to_1_5_lst","rand_pp_cnt_0_5_to_1_5_lst","rand_pp_cnt_1_5_to_3_5_lst","rand_pp_cnt_3_5_to_7_lst","rand_pp_cnt_7_to_15_lst","rand_np_cnt_0_to_0_25_lst","rand_np_cnt_0_25_to_0_5_lst","rand_np_cnt_0_to_0_5_lst","rand_np_cnt_0_5_to_1_lst","rand_np_cnt_1_to_1_5_lst","rand_np_cnt_0_5_to_1_5_lst","rand_np_cnt_1_5_to_3_5_lst","rand_np_cnt_3_5_to_7_lst","rand_np_cnt_7_to_15_lst","all_swing_avg_time","pstv_swing_avg_time","neg_swing_avg_time","top_10_lrg_pstv_total_rand_per_change","top_10_lrg_pstv_avg_time","top_10_sml_pstv_total_rand_per_change","top_10_sml_pstv_avg_time","top_10_lrg_neg_avg_time","top_10_sml_neg_avg_time","zero_rand_avg_swings_time","zero_rand_pstv_sp_avg_swings_time","zero_rand_neg_sp_avg_swings_time","all_swing_avg_rsi_diff","pstv_swing_avg_rsi_diff","neg_swing_avg_rsi_diff","top_10_lrg_pstv_avg_rsi_diff","top_10_sml_pstv_avg_rsi_diff","top_10_lrg_neg_avg_rsi_diff","top_10_sml_neg_avg_rsi_diff","zero_rand_avg_swings_rsi_diff","zero_rand_pstv_sp_avg_rsi_diff","zero_rand_neg_sp_avg_swings_rsi_diff","total_fb","total_pstv_fb","total_neg_fb"]

layer_3_rank_6_col_names = [
    "coin_name","coin_time_tf","last_swing_per","last_swing_rand_per","last_swing_time","last_swing_rsi_dif","last_3_s_per_avg","last_3_s_rand_avg","last_3_s_avg_time","last_3_s_rsi_diff_avg","all_swing_count","all_swings_pp_count","all_swings_np_count","all_swings_pp_med","all_swings_np_med","t_10_lrg_pp_sp_med","t_10_lrg_np_sp_med","t_10_sml_pp_sp_med","t_10_sml_np_sp_med","sp_pp_cnt_0_2_lst","sp_pp_cnt_2_4_lst","sp_pp_cnt_4_7_lst","sp_pp_cnt_7_15_lst","sp_pp_cnt_15_25_lst","sp_np_cnt_0_2_lst","sp_np_cnt_2_4_lst","sp_np_cnt_4_7_lst","sp_np_cnt_7_15_lst","sp_np_cnt_15_25_lst","all_swings_rand_pp_med","all_swings_rand_np_med","t_10_lrg_pp_rand_sp_med","t_10_lrg_np_rand_sp_med","t_10_sml_pp_rand_sp_med","t_10_sml_np_rand_sp_med","all_swings_zero_rand_count","all_swings_zero_rand_pp_count","all_swings_zero_rand_np_count","all_swings_zero_rand_pp_med","all_swings_zero_rand_np_med","t_10_lrg_pp_zero_rand_sp_med","t_10_lrg_np_zero_rand_sp_med","t_10_sml_pp_zero_rand_sp_med","t_10_sml_np_zero_rand_sp_med","rand_pp_cnt_0_to_0_25_lst","rand_pp_cnt_0_25_to_0_5_lst","rand_pp_cnt_0_to_0_5_lst","rand_pp_cnt_0_5_to_1_lst","rand_pp_cnt_1_to_1_5_lst","rand_pp_cnt_0_5_to_1_5_lst","rand_pp_cnt_1_5_to_3_5_lst","rand_pp_cnt_3_5_to_7_lst","rand_pp_cnt_7_to_15_lst","rand_np_cnt_0_to_0_25_lst","rand_np_cnt_0_25_to_0_5_lst","rand_np_cnt_0_to_0_5_lst","rand_np_cnt_0_5_to_1_lst","rand_np_cnt_1_to_1_5_lst","rand_np_cnt_0_5_to_1_5_lst","rand_np_cnt_1_5_to_3_5_lst","rand_np_cnt_3_5_to_7_lst","rand_np_cnt_7_to_15_lst","all_swing_median_time","pstv_swing_median_time","neg_swing_median_time","top_10_lrg_pstv_total_rand_per_change","top_10_lrg_pstv_median_time","top_10_sml_pstv_total_rand_per_change","top_10_sml_pstv_median_time","top_10_lrg_neg_median_time","top_10_sml_neg_median_time","zero_rand_med_swings_time","zero_rand_pstv_sp_med_swings_time","zero_rand_neg_sp_med_swings_time","all_swing_median_rsi_diff","pstv_swing_median_rsi_diff","neg_swing_median_rsi_diff","top_10_sml_pstv_median_rsi_diff","top_10_lrg_neg_median_rsi_diff","top_10_sml_neg_median_rsi_diff","zero_rand_med_swings_rsi_diff","zero_rand_pstv_sp_med_swings_rsi_diff","zero_rand_neg_sp_med_swings_rsi_diff","total_fb","total_pstv_fb","total_neg_fb"]

binance_coins = [
    "REEFUSDT.P", "1000FLOKIUSDT.P", "1000BONKUSDT.P", "1000SHIBUSDT.P", "PEOPLEUSDT.P",
    "1000PEPEUSDT.P", "NOTUSDT.P", "WUSDT.P", "BOMEUSDT.P", "SYSUSDT.P", "CFXUSDT.P",
    "SKLUSDT.P", "BANANAUSDT.P", "TURBOUSDT.P", "JASMYUSDT.P", "1000XECUSDT.P",
    "RSRUSDT.P", "DOGEUSDT.P", "OPUSDT.P", "FXSUSDT.P", "COMBOUSDT.P", "MYROUSDT.P",
    "PHBUSDT.P", "DOGSUSDT.P", "VANRYUSDT.P", "LDOUSDT.P", "WIFUSDT.P", "MEMEUSDT.P",
    "NKNUSDT.P", "GALAUSDT.P", "ACHUSDT.P", "KASUSDT.P", "CRVUSDT.P", "ENJUSDT.P",
    "VOXELUSDT.P", "ILVUSDT.P", "C98USDT.P", "GUSDT.P", "ARBUSDT.P", "SPELLUSDT.P",
    "ALTUSDT.P", "MAVIAUSDT.P", "YGGUSDT.P", "CAKEUSDT.P", "ORDIUSDT.P", "PIXELUSDT.P",
    "VETUSDT.P", "ENSUSDT.P", "SUSHIUSDT.P", "RENDERUSDT.P", "TOKENUSDT.P", "WLDUSDT.P",
    "XVGUSDT.P", "HIGHUSDT.P", "AUCTIONUSDT.P", "AMBUSDT.P", "RPLUSDT.P", "1000LUNCUSDT.P",
    "MKRUSDT.P", "ROSEUSDT.P", "ZKUSDT.P", "DENTUSDT.P", "HOTUSDT.P", "ZILUSDT.P",
    "SYNUSDT.P", "TRUUSDT.P", "TRBUSDT.P", "UMAUSDT.P", "REZUSDT.P", "AVAXUSDT.P",
    "LUNA2USDT.P", "TONUSDT.P", "STRKUSDT.P", "ONEUSDT.P", "1000SATSUSDT.P", "SANDUSDT.P",
    "BICOUSDT.P", "USTCUSDT.P", "CHESSUSDT.P", "DUSKUSDT.P", "GTCUSDT.P", "TIAUSDT.P",
    "MOVRUSDT.P", "NTRNUSDT.P", "RAREUSDT.P", "ETHFIUSDT.P", "JOEUSDT.P", "TWTUSDT.P",
    "ALICEUSDT.P", "MANAUSDT.P", "APTUSDT.P", "AAVEUSDT.P", "BRETTUSDT.P", "TNSRUSDT.P",
    "BSVUSDT.P", "ATOMUSD.P", "CYBERUSDT.P", "ATOMUSDT.P", "1MBABYDOGEUSDT.P", "ARUSDT.P",
    "BCHUSDT.P", "ICPUSDT.P", "JTOUSDT.P", "AIUSDT.P", "BADGERUSDT.P", "ONDOUSDT.P",
    "TLMUSDT.P", "DYMUSDT.P", "SUIUSDT.P", "CATIUSDT.P", "RENUSDT.P", "QTUMUSDT.P",
    "RDNTUSDT.P", "LINAUSDT.P", "ALPHAUSDT.P", "FETUSDT.P", "ATAUSDT.P", "UNFIUSDT.P",
    "BSWUSDT.P", "XAIUSDT.P", "FILUSDT.P", "XVSUSDT.P", "SOLUSDT.P", "FLUXUSDT.P",
    "PORTALUSDT.P", "LTCUSD.P", "LTCUSDT.P", "KAVAUSDT.P", "YFIUSDT.P", "UNIUSDT.P",
    "ETCUSDT.P", "BNBUSDT.P", "BALUSDT.P", "DEFIUSDT.P", "GRTUSDT.P", "HMSTRUSDT.P",
    "TAOUSDT.P", "AEVOUSDT.P", "BIGTIMEUSDT.P", "MANTAUSDT.P", "FIOUSDT.P", "ETHUSDT.P",
    "ZRXUSDT.P", "DYDXUSDT.P", "ACEUSDT.P", "ANKRUSDT.P", "XTZUSDT.P", "POLUSDT.P",
    "UXLINKUSDT.P", "NMRUSDT.P", "SSVUSDT.P", "API3USDT.P", "DOTUSDT.P", "KEYUSDT.P",
    "ZETAUSDT.P", "1INCHUSDT.P", "EGLDUSDT.P", "AXLUSDT.P", "ALGOUSDT.P", "IOTAUSDT.P",
    "APEUSDT.P", "LITUSDT.P", "BNTUSDT.P", "AXSUSDT.P", "FLMUSDT.P", "JUPUSDT.P",
    "RIFUSDT.P", "IMXUSDT.P", "SXPUSDT.P", "WAXPUSDT.P", "NFPUSDT.P", "ZENUSDT.P",
    "TRXUSDT.P", "IOSTUSDT.P", "RLCUSDT.P", "MASKUSDT.P", "LPTUSDT.P", "LQTYUSDT.P",
    "BTCUSDT.P", "CTSIUSDT.P", "PERPUSDT.P", "CKBUSDT.P", "KLAYUSDT.P", "MBOXUSDT.P",
    "DASHUSDT.P", "COMPUSDT.P", "MAGICUSDT.P", "KSMUSDT.P", "LINKUSD.P", "QNTUSDT.P",
    "LINKUSDT.P", "BAKEUSDT.P", "RVNUSDT.P", "ICXUSDT.P", "FLOWUSDT.P", "MAVUSDT.P",
    "FTMUSD.P", "PYTHUSDT.P", "FTMUSDT.P", "NULSUSDT.P", "SNXUSDT.P", "HFTUSDT.P",
    "IDUSDT.P", "ARKMUSDT.P", "ZECUSDT.P", "BEAMXUSDT.P", "METISUSDT.P", "EOSUSDT.P",
    "ORBSUSDT.P", "LRCUSDT.P", "INJUSDT.P", "BONDUSDT.P", "SUPERUSDT.P", "CHRUSDT.P",
    "LEVERUSDT.P", "LSKUSDT.P", "GMXUSDT.P", "ALPACAUSDT.P", "ADAUSDT.P", "ETHWUSDT.P",
    "BATUSDT.P", "DODOXUSDT.P", "ADAUSD.P", "GMTUSDT.P", "STXUSDT.P", "TUSDT.P",
    "EDUUSDT.P", "MTLUSDT.P", "STMXUSDT.P", "GLMUSDT.P", "ONGUSDT.P", "DARUSDT.P",
    "XEMUSDT.P", "PENDLEUSDT.P", "XLMUSDT.P", "1000RATSUSDT.P", "OXTUSDT.P", "GHSTUSDT.P",
    "LOKAUSDT.P", "RUNEUSDT.P", "ONTUSDT.P", "BLURUSDT.P", "OMGUSDT.P", "ARPAUSDT.P",
    "SFPUSDT.P", "BANDUSDT.P", "BNXUSDT.P", "NEOUSDT.P", "KDAUSDT.P", "ZROUSDT.P",
    "CELRUSDT.P", "ASTRUSDT.P", "THETAUSDT.P", "WOOUSDT.P", "FIDAUSDT.P", "KNCUSDT.P",
    "GASUSDT.P", "STGUSDT.P", "RONINUSDT.P", "LISTAUSDT.P", "CHZUSDT.P", "QUICKUSDT.P",
    "HBARUSDT.P", "POLYXUSDT.P", "BELUSDT.P", "XRPUSD.P", "XRPUSDT.P", "STORJUSDT.P",
    "HIFIUSDT.P", "POWRUSDT.P", "MINAUSDT.P", "BLZUSDT.P", "CELOUSDT.P", "OGNUSDT.P",
    "SUNUSDT.P", "STEEMUSDT.P", "BTCDOMUSDT.P", "NEIROUSDT.P", "IOTXUSDT.P", "XMRUSDT.P",
    "ARKUSDT.P", "COTIUSDT.P", "OMUSDT.P", "LOOMUSDT.P", "NEARUSDT.P", "SEIUSDT.P","AERGOUSDT.P","IOUSDT.P","HOOKUSDT.P","SAGAUSDT.P","BBUSDT.P","NEIROETHUSDT.P","OMNIUSDT.P","AGLDUSDT.P","ENAUSDT.P","MEWUSDT.P","POPCATUSDT.P","VIDTUSDT.P"]