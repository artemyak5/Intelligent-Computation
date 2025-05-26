from controller import MulticookerController
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mc = MulticookerController()

    labels = [
        'rice', 'soup', 'porridge', 'stew', 'steam',
        'keep_warm', 'bake', 'yogurt', 'reheat', 'sterilization'
    ]
    test_cases = [
        {'dish': 0, 'volume': 1.0, 'ratio': 2.0, 'temp_in': 20.0},
        {'dish': 1, 'volume': 3.0, 'ratio': 2.5, 'temp_in': 10.0},
        {'dish': 2, 'volume': 2.0, 'ratio': 2.5, 'temp_in': 15.0},
        {'dish': 3, 'volume': 4.0, 'ratio': 2.5, 'temp_in': 5.0},
        {'dish': 4, 'volume': 0.5, 'ratio': 1.0, 'temp_in': 25.0},
        {'dish': 5, 'volume': 4.5, 'ratio': 1.5, 'temp_in': 25.0},
        {'dish': 6, 'volume': 3.0, 'ratio': 1.5, 'temp_in': 20.0},
        {'dish': 7, 'volume': 1.0, 'ratio': 2.0, 'temp_in': 15.0},
        {'dish': 8, 'volume': 2.0, 'ratio': 1.8, 'temp_in': 30.0},
        {'dish': 9, 'volume': 2.0, 'ratio': 2.0, 'temp_in': 5.0},
    ]

    print("Results for all dish modes:")
    for case in test_cases:
        time_pred, temp_pred = mc.compute(
            case['volume'], case['ratio'], case['temp_in'], case['dish']
        )
        print(
            f"{labels[case['dish']]:12s} | volume={case['volume']:.1f}L, "
            f"ratio={case['ratio']:.1f}, temp_in={case['temp_in']:.1f}°C -> "
            f"cook_time={time_pred:.2f}min, cook_temp={temp_pred:.2f}°C"
        )

    # Візуалізація функцій приналежності
    mc.volume.view()
    mc.ratio.view()
    mc.temp_in.view()
    mc.dish.view()
    mc.cook_time.view()
    mc.cook_temp.view()
    plt.tight_layout()
    plt.show()
