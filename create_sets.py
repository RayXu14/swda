import os
import shutil

# Data split from Lee & Dernoncourt (2016)
# https://github.com/Franck-Dernoncourt/naacl2016
TRAIN_SET_IDX = ['sw2005', 'sw2006', 'sw2008', 'sw2010', 'sw2012', 'sw2015', 'sw2018', 'sw2019', 'sw2020', 'sw2022',
                 'sw2024', 'sw2025', 'sw2027', 'sw2028', 'sw2032', 'sw2035', 'sw2038', 'sw2039', 'sw2040', 'sw2041',
                 'sw2051', 'sw2060', 'sw2061', 'sw2062', 'sw2064', 'sw2065', 'sw2073', 'sw2078', 'sw2079', 'sw2085',
                 'sw2086', 'sw2090', 'sw2092', 'sw2093', 'sw2094', 'sw2095', 'sw2101', 'sw2102', 'sw2104', 'sw2105',
                 'sw2107', 'sw2109', 'sw2110', 'sw2111', 'sw2113', 'sw2120', 'sw2122', 'sw2124', 'sw2125', 'sw2130',
                 'sw2137', 'sw2139', 'sw2145', 'sw2149', 'sw2154', 'sw2155', 'sw2157', 'sw2168', 'sw2171', 'sw2177',
                 'sw2178', 'sw2180', 'sw2181', 'sw2184', 'sw2185', 'sw2187', 'sw2190', 'sw2191', 'sw2197', 'sw2205',
                 'sw2220', 'sw2221', 'sw2226', 'sw2227', 'sw2228', 'sw2231', 'sw2232', 'sw2234', 'sw2235', 'sw2237',
                 'sw2241', 'sw2244', 'sw2247', 'sw2248', 'sw2249', 'sw2252', 'sw2259', 'sw2260', 'sw2262', 'sw2263',
                 'sw2264', 'sw2265', 'sw2266', 'sw2268', 'sw2275', 'sw2278', 'sw2279', 'sw2283', 'sw2285', 'sw2287',
                 'sw2290', 'sw2292', 'sw2293', 'sw2295', 'sw2296', 'sw2300', 'sw2301', 'sw2302', 'sw2303', 'sw2304',
                 'sw2305', 'sw2308', 'sw2309', 'sw2313', 'sw2314', 'sw2316', 'sw2323', 'sw2324', 'sw2325', 'sw2330',
                 'sw2331', 'sw2334', 'sw2336', 'sw2339', 'sw2342', 'sw2344', 'sw2349', 'sw2353', 'sw2354', 'sw2355',
                 'sw2362', 'sw2365', 'sw2366', 'sw2368', 'sw2370', 'sw2372', 'sw2376', 'sw2379', 'sw2380', 'sw2382',
                 'sw2383', 'sw2386', 'sw2387', 'sw2389', 'sw2393', 'sw2397', 'sw2405', 'sw2406', 'sw2407', 'sw2413',
                 'sw2418', 'sw2421', 'sw2423', 'sw2424', 'sw2426', 'sw2427', 'sw2429', 'sw2431', 'sw2432', 'sw2433',
                 'sw2435', 'sw2436', 'sw2437', 'sw2439', 'sw2442', 'sw2445', 'sw2446', 'sw2448', 'sw2450', 'sw2451',
                 'sw2452', 'sw2457', 'sw2460', 'sw2465', 'sw2466', 'sw2467', 'sw2469', 'sw2471', 'sw2472', 'sw2476',
                 'sw2477', 'sw2478', 'sw2479', 'sw2482', 'sw2483', 'sw2485', 'sw2486', 'sw2488', 'sw2490', 'sw2492',
                 'sw2495', 'sw2499', 'sw2502', 'sw2504', 'sw2506', 'sw2510', 'sw2511', 'sw2514', 'sw2515', 'sw2519',
                 'sw2521', 'sw2524', 'sw2525', 'sw2526', 'sw2527', 'sw2528', 'sw2533', 'sw2537', 'sw2539', 'sw2540',
                 'sw2543', 'sw2545', 'sw2546', 'sw2547', 'sw2548', 'sw2549', 'sw2552', 'sw2554', 'sw2557', 'sw2559',
                 'sw2562', 'sw2565', 'sw2566', 'sw2568', 'sw2570', 'sw2571', 'sw2575', 'sw2576', 'sw2578', 'sw2579',
                 'sw2584', 'sw2585', 'sw2586', 'sw2587', 'sw2589', 'sw2597', 'sw2599', 'sw2602', 'sw2603', 'sw2604',
                 'sw2608', 'sw2609', 'sw2610', 'sw2611', 'sw2614', 'sw2615', 'sw2616', 'sw2617', 'sw2619', 'sw2622',
                 'sw2627', 'sw2628', 'sw2631', 'sw2634', 'sw2638', 'sw2640', 'sw2641', 'sw2642', 'sw2645', 'sw2647',
                 'sw2648', 'sw2650', 'sw2652', 'sw2657', 'sw2658', 'sw2661', 'sw2662', 'sw2663', 'sw2667', 'sw2669',
                 'sw2672', 'sw2675', 'sw2676', 'sw2678', 'sw2679', 'sw2684', 'sw2689', 'sw2690', 'sw2691', 'sw2692',
                 'sw2693', 'sw2703', 'sw2707', 'sw2708', 'sw2709', 'sw2710', 'sw2711', 'sw2716', 'sw2717', 'sw2719',
                 'sw2723', 'sw2726', 'sw2729', 'sw2734', 'sw2736', 'sw2741', 'sw2743', 'sw2744', 'sw2749', 'sw2751',
                 'sw2754', 'sw2756', 'sw2759', 'sw2761', 'sw2766', 'sw2767', 'sw2768', 'sw2770', 'sw2773', 'sw2774',
                 'sw2775', 'sw2780', 'sw2782', 'sw2784', 'sw2785', 'sw2788', 'sw2789', 'sw2792', 'sw2793', 'sw2794',
                 'sw2797', 'sw2800', 'sw2803', 'sw2806', 'sw2812', 'sw2818', 'sw2819', 'sw2820', 'sw2821', 'sw2826',
                 'sw2827', 'sw2828', 'sw2830', 'sw2834', 'sw2835', 'sw2837', 'sw2840', 'sw2844', 'sw2847', 'sw2849',
                 'sw2851', 'sw2858', 'sw2860', 'sw2862', 'sw2866', 'sw2868', 'sw2870', 'sw2871', 'sw2875', 'sw2876',
                 'sw2877', 'sw2879', 'sw2883', 'sw2884', 'sw2887', 'sw2893', 'sw2896', 'sw2897', 'sw2898', 'sw2900',
                 'sw2909', 'sw2910', 'sw2913', 'sw2915', 'sw2917', 'sw2921', 'sw2924', 'sw2926', 'sw2927', 'sw2929',
                 'sw2930', 'sw2932', 'sw2934', 'sw2935', 'sw2938', 'sw2942', 'sw2945', 'sw2950', 'sw2952', 'sw2953',
                 'sw2954', 'sw2955', 'sw2956', 'sw2957', 'sw2960', 'sw2962', 'sw2963', 'sw2965', 'sw2967', 'sw2968',
                 'sw2969', 'sw2970', 'sw2982', 'sw2983', 'sw2984', 'sw2991', 'sw2992', 'sw2993', 'sw2994', 'sw2995',
                 'sw2996', 'sw2998', 'sw2999', 'sw3000', 'sw3001', 'sw3002', 'sw3003', 'sw3004', 'sw3007', 'sw3009',
                 'sw3011', 'sw3012', 'sw3013', 'sw3014', 'sw3016', 'sw3018', 'sw3019', 'sw3020', 'sw3021', 'sw3023',
                 'sw3025', 'sw3028', 'sw3029', 'sw3030', 'sw3034', 'sw3036', 'sw3038', 'sw3039', 'sw3040', 'sw3041',
                 'sw3042', 'sw3045', 'sw3047', 'sw3049', 'sw3050', 'sw3051', 'sw3052', 'sw3054', 'sw3055', 'sw3056',
                 'sw3057', 'sw3059', 'sw3061', 'sw3062', 'sw3063', 'sw3064', 'sw3065', 'sw3067', 'sw3068', 'sw3069',
                 'sw3070', 'sw3071', 'sw3073', 'sw3074', 'sw3075', 'sw3076', 'sw3077', 'sw3080', 'sw3081', 'sw3082',
                 'sw3083', 'sw3085', 'sw3086', 'sw3087', 'sw3088', 'sw3090', 'sw3092', 'sw3093', 'sw3095', 'sw3097',
                 'sw3099', 'sw3102', 'sw3103', 'sw3104', 'sw3105', 'sw3107', 'sw3108', 'sw3111', 'sw3113', 'sw3115',
                 'sw3118', 'sw3120', 'sw3121', 'sw3124', 'sw3130', 'sw3131', 'sw3133', 'sw3134', 'sw3135', 'sw3136',
                 'sw3138', 'sw3140', 'sw3142', 'sw3143', 'sw3144', 'sw3146', 'sw3150', 'sw3151', 'sw3152', 'sw3154',
                 'sw3155', 'sw3158', 'sw3159', 'sw3161', 'sw3162', 'sw3166', 'sw3167', 'sw3168', 'sw3169', 'sw3170',
                 'sw3171', 'sw3173', 'sw3174', 'sw3175', 'sw3182', 'sw3185', 'sw3186', 'sw3187', 'sw3188', 'sw3189',
                 'sw3194', 'sw3195', 'sw3196', 'sw3198', 'sw3200', 'sw3201', 'sw3203', 'sw3204', 'sw3205', 'sw3206',
                 'sw3208', 'sw3214', 'sw3215', 'sw3216', 'sw3219', 'sw3221', 'sw3223', 'sw3225', 'sw3226', 'sw3227',
                 'sw3228', 'sw3229', 'sw3230', 'sw3231', 'sw3232', 'sw3233', 'sw3234', 'sw3235', 'sw3236', 'sw3237',
                 'sw3238', 'sw3242', 'sw3244', 'sw3245', 'sw3247', 'sw3252', 'sw3253', 'sw3254', 'sw3256', 'sw3259',
                 'sw3260', 'sw3265', 'sw3266', 'sw3267', 'sw3268', 'sw3269', 'sw3270', 'sw3271', 'sw3272', 'sw3275',
                 'sw3276', 'sw3279', 'sw3280', 'sw3282', 'sw3283', 'sw3284', 'sw3286', 'sw3293', 'sw3294', 'sw3296',
                 'sw3300', 'sw3303', 'sw3304', 'sw3306', 'sw3309', 'sw3310', 'sw3311', 'sw3313', 'sw3315', 'sw3317',
                 'sw3319', 'sw3320', 'sw3324', 'sw3325', 'sw3326', 'sw3327', 'sw3328', 'sw3330', 'sw3331', 'sw3332',
                 'sw3333', 'sw3338', 'sw3340', 'sw3342', 'sw3343', 'sw3344', 'sw3345', 'sw3349', 'sw3351', 'sw3353',
                 'sw3355', 'sw3359', 'sw3360', 'sw3361', 'sw3362', 'sw3363', 'sw3364', 'sw3365', 'sw3367', 'sw3368',
                 'sw3369', 'sw3371', 'sw3372', 'sw3373', 'sw3375', 'sw3377', 'sw3379', 'sw3381', 'sw3383', 'sw3384',
                 'sw3386', 'sw3387', 'sw3389', 'sw3393', 'sw3397', 'sw3398', 'sw3399', 'sw3402', 'sw3403', 'sw3405',
                 'sw3406', 'sw3408', 'sw3409', 'sw3411', 'sw3414', 'sw3417', 'sw3419', 'sw3420', 'sw3421', 'sw3424',
                 'sw3425', 'sw3426', 'sw3427', 'sw3428', 'sw3429', 'sw3431', 'sw3435', 'sw3439', 'sw3441', 'sw3443',
                 'sw3447', 'sw3448', 'sw3449', 'sw3450', 'sw3451', 'sw3453', 'sw3454', 'sw3455', 'sw3457', 'sw3458',
                 'sw3460', 'sw3463', 'sw3464', 'sw3467', 'sw3473', 'sw3476', 'sw3487', 'sw3489', 'sw3495', 'sw3496',
                 'sw3503', 'sw3504', 'sw3508', 'sw3513', 'sw3514', 'sw3515', 'sw3517', 'sw3518', 'sw3521', 'sw3523',
                 'sw3524', 'sw3525', 'sw3526', 'sw3527', 'sw3530', 'sw3533', 'sw3535', 'sw3537', 'sw3539', 'sw3541',
                 'sw3543', 'sw3549', 'sw3550', 'sw3551', 'sw3556', 'sw3557', 'sw3561', 'sw3563', 'sw3565', 'sw3567',
                 'sw3569', 'sw3570', 'sw3573', 'sw3574', 'sw3580', 'sw3586', 'sw3591', 'sw3595', 'sw3596', 'sw3597',
                 'sw3606', 'sw3607', 'sw3615', 'sw3624', 'sw3626', 'sw3628', 'sw3633', 'sw3636', 'sw3638', 'sw3639',
                 'sw3642', 'sw3646', 'sw3647', 'sw3651', 'sw3655', 'sw3657', 'sw3660', 'sw3662', 'sw3663', 'sw3665',
                 'sw3676', 'sw3680', 'sw3681', 'sw3682', 'sw3688', 'sw3691', 'sw3692', 'sw3693', 'sw3694', 'sw3696',
                 'sw3699', 'sw3703', 'sw3707', 'sw3709', 'sw3716', 'sw3720', 'sw3723', 'sw3725', 'sw3727', 'sw3728',
                 'sw3734', 'sw3735', 'sw3736', 'sw3738', 'sw3743', 'sw3745', 'sw3746', 'sw3747', 'sw3750', 'sw3751',
                 'sw3754', 'sw3760', 'sw3763', 'sw3764', 'sw3768', 'sw3770', 'sw3773', 'sw3774', 'sw3776', 'sw3777',
                 'sw3781', 'sw3784', 'sw3788', 'sw3791', 'sw3796', 'sw3798', 'sw3801', 'sw3802', 'sw3803', 'sw3804',
                 'sw3805', 'sw3809', 'sw3813', 'sw3815', 'sw3821', 'sw3825', 'sw3828', 'sw3830', 'sw3838', 'sw3841',
                 'sw3845', 'sw3847', 'sw3850', 'sw3852', 'sw3855', 'sw3862', 'sw3870', 'sw3876', 'sw3883', 'sw3887',
                 'sw3898', 'sw3902', 'sw3903', 'sw3908', 'sw3911', 'sw3917', 'sw3925', 'sw3926', 'sw3946', 'sw3952',
                 'sw3956', 'sw3962', 'sw3965', 'sw3971', 'sw3979', 'sw3983', 'sw3985', 'sw3988', 'sw3993', 'sw4008',
                 'sw4013', 'sw4019', 'sw4022', 'sw4023', 'sw4028', 'sw4032', 'sw4033', 'sw4036', 'sw4038', 'sw4049',
                 'sw4050', 'sw4051', 'sw4055', 'sw4056', 'sw4060', 'sw4064', 'sw4071', 'sw4074', 'sw4077', 'sw4078',
                 'sw4079', 'sw4080', 'sw4082', 'sw4090', 'sw4092', 'sw4096', 'sw4099', 'sw4101', 'sw4103', 'sw4104',
                 'sw4108', 'sw4109', 'sw4113', 'sw4114', 'sw4123', 'sw4127', 'sw4129', 'sw4130', 'sw4133', 'sw4137',
                 'sw4138', 'sw4147', 'sw4148', 'sw4149', 'sw4150', 'sw4151', 'sw4152', 'sw4153', 'sw4154', 'sw4155',
                 'sw4158', 'sw4159', 'sw4165', 'sw4166', 'sw4168', 'sw4171', 'sw4174', 'sw4175', 'sw4177', 'sw4181',
                 'sw4184', 'sw4311', 'sw4312', 'sw4314', 'sw4316', 'sw4319', 'sw4320', 'sw4325', 'sw4327', 'sw4329',
                 'sw4330', 'sw4333', 'sw4334', 'sw4336', 'sw4339', 'sw4340', 'sw4341', 'sw4342', 'sw4345', 'sw4346',
                 'sw4349', 'sw4353', 'sw4358', 'sw4360', 'sw4362', 'sw4363', 'sw4364', 'sw4366', 'sw4370', 'sw4376',
                 'sw4378', 'sw4379', 'sw4380', 'sw4382', 'sw4443', 'sw4483', 'sw4519', 'sw4548', 'sw4565', 'sw4603',
                 'sw4605', 'sw4608', 'sw4611', 'sw4615', 'sw4617', 'sw4618', 'sw4619', 'sw4626', 'sw4628', 'sw4630',
                 'sw4642', 'sw4644', 'sw4646', 'sw4649', 'sw4655', 'sw4659', 'sw4666', 'sw4675', 'sw4679', 'sw4681',
                 'sw4682', 'sw4688', 'sw4691', 'sw4698', 'sw4703', 'sw4709', 'sw4720', 'sw4721', 'sw4723', 'sw4725',
                 'sw4726', 'sw4728', 'sw4733', 'sw4735', 'sw4745', 'sw4752', 'sw4758', 'sw4759', 'sw4765', 'sw4770',
                 'sw4774', 'sw4784', 'sw4785', 'sw4788', 'sw4792', 'sw4796', 'sw4799', 'sw4801', 'sw4812', 'sw4814',
                 'sw4821', 'sw4822', 'sw4826', 'sw4829', 'sw4830', 'sw4831', 'sw4834', 'sw4840', 'sw4856', 'sw4858',
                 'sw4859', 'sw4868', 'sw4876', 'sw4877', 'sw4880', 'sw4886', 'sw4902', 'sw4905', 'sw4908', 'sw4927',
                 'sw4928', 'sw4936', 'sw4940']
# TRAIN_SET_IDX = ['sw2005']
VALID_SET_IDX = ['sw2053', 'sw2067', 'sw2071', 'sw2072', 'sw2160', 'sw2163', 'sw2175', 'sw2253', 'sw2289', 'sw2299',
                 'sw2340', 'sw2373', 'sw2395', 'sw2399', 'sw2455', 'sw2501', 'sw2534', 'sw2558', 'sw2593', 'sw2594',
                 'sw2598', 'sw2620', 'sw2621', 'sw2623', 'sw2630', 'sw2653', 'sw2713', 'sw2755', 'sw2772', 'sw2776',
                 'sw2790', 'sw2832', 'sw2839', 'sw2842', 'sw2854', 'sw2874', 'sw2888', 'sw2889', 'sw2944', 'sw2959',
                 'sw2981', 'sw2989', 'sw3015', 'sw3046', 'sw3072', 'sw3096', 'sw3148', 'sw3156', 'sw3181', 'sw3184',
                 'sw3190', 'sw3191', 'sw3202', 'sw3207', 'sw3239', 'sw3246', 'sw3250', 'sw3251', 'sw3255', 'sw3257',
                 'sw3281', 'sw3288', 'sw3290', 'sw3291', 'sw3334', 'sw3346', 'sw3352', 'sw3354', 'sw3382', 'sw3433',
                 'sw3445', 'sw3491', 'sw3497', 'sw3500', 'sw3506', 'sw3509', 'sw3554', 'sw3576', 'sw3584', 'sw3587',
                 'sw3658', 'sw3659', 'sw3666', 'sw3675', 'sw3686', 'sw3697', 'sw3711', 'sw3769', 'sw3797', 'sw3810',
                 'sw3811', 'sw3921', 'sw4004', 'sw4026', 'sw4037', 'sw4048', 'sw4072', 'sw4318', 'sw4321', 'sw4347',
                 'sw4356', 'sw4372', 'sw4572', 'sw4633', 'sw4660', 'sw4697', 'sw4707', 'sw4716', 'sw4736', 'sw4802',
                 'sw4890', 'sw4917']
# VALID_SET_IDX = ['sw2053']
TEST_SET_IDX = ['sw2121', 'sw2131', 'sw2151', 'sw2229', 'sw2335', 'sw2434', 'sw2441', 'sw2461', 'sw2503', 'sw2632',
                'sw2724', 'sw2752', 'sw2753', 'sw2836', 'sw2838', 'sw3528', 'sw3756', 'sw3942', 'sw3994']
# TEST_SET_IDX = ['sw2121']
assert len(TRAIN_SET_IDX + VALID_SET_IDX + TEST_SET_IDX) == 1115 + 19  # 1115 seen dialogs, 19 unseen dialogs.


def build_tree(dest_path):
    """
    Create directory tree to divide data
    """
    sets_dir = os.path.join(dest_path, 'sets')
    if os.path.isdir(sets_dir):
        shutil.rmtree(sets_dir)
    os.mkdir(sets_dir)
    train_dir = os.path.join(sets_dir, 'train', 'sw0')
    os.makedirs(train_dir)
    valid_dir = os.path.join(sets_dir, 'valid', 'sw0')
    os.makedirs(valid_dir)
    test_dir = os.path.join(sets_dir, 'test', 'sw0')
    os.makedirs(test_dir)


def mv_files(dest_path, data_path):
    """
    Divide files depending on their names
    """
    train_path = os.path.join(dest_path, 'sets', 'train')
    valid_path = os.path.join(dest_path, 'sets', 'valid')
    test_path = os.path.join(dest_path, 'sets', 'test')

    for root, directories, files in os.walk(data_path):
        for file in files:
            f_name, f_ext = os.path.splitext(file)
            if f_ext == ".csv":
                if f_name == 'swda-metadata':
                    shutil.copyfile(os.path.join(root, file), os.path.join(train_path, file))
                    shutil.copyfile(os.path.join(root, file), os.path.join(valid_path, file))
                    shutil.copyfile(os.path.join(root, file), os.path.join(test_path, file))
                f_name, f_ext = os.path.splitext(f_name)
                if f_ext == ".utt":
                    chunks = f_name.split('_')
                    fileID = chunks[0] + chunks[2]
                    file_path = os.path.join(root, file)
                    if fileID in TRAIN_SET_IDX:
                        shutil.copyfile(file_path, os.path.join(train_path, 'sw0', file))
                    elif fileID in VALID_SET_IDX:
                        shutil.copyfile(file_path, os.path.join(valid_path, 'sw0', file))
                    elif fileID in TEST_SET_IDX:
                        shutil.copyfile(file_path, os.path.join(test_path, 'sw0', file))


def main(dest_path, data_path):
    build_tree(dest_path)
    mv_files(dest_path, data_path)


DEST_PATH = '.'
DATA_PATH = os.path.join(DEST_PATH, 'swda')

main(DEST_PATH, DATA_PATH)
