from controller import MulticookerController
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mc = MulticookerController()

    # Labels for dish codes
    labels = ['rice', 'soup', 'porridge', 'stew', 'steam', 'keep_warm', 'bake', 'yogurt', 'reheat', 'sterilization']

    # Тестові випадки для кожного режиму страви
    test_cases = [
        {'dish': 0, 'volume': 1.0, 'ratio': 2.0, 'temp_in': 20.0},  # rice
        {'dish': 1, 'volume': 3.0, 'ratio': 2.5, 'temp_in': 10.0},  # soup
        {'dish': 2, 'volume': 2.0, 'ratio': 2.5, 'temp_in': 15.0},  # porridge
        {'dish': 3, 'volume': 4.0, 'ratio': 2.5, 'temp_in': 5.0},   # stew
        {'dish': 4, 'volume': 0.5, 'ratio': 1.0, 'temp_in': 25.0},  # steam
        {'dish': 5, 'volume': 4.5, 'ratio': 1.5, 'temp_in': 25.0},  # keep_warm
        {'dish': 6, 'volume': 3.0, 'ratio': 1.5, 'temp_in': 20.0},  # bake
        {'dish': 7, 'volume': 1.0, 'ratio': 2.0, 'temp_in': 15.0},  # yogurt
        {'dish': 8, 'volume': 2.0, 'ratio': 1.8, 'temp_in': 30.0},  # reheat
        {'dish': 9, 'volume': 2.0, 'ratio': 2.0, 'temp_in': 5.0},   # sterilization
    ]

    print("Results for all dish modes:")
    for case in test_cases:
        time_pred, temp_pred = mc.compute(case['volume'], case['ratio'], case['temp_in'], case['dish'])
        print(f"{labels[case['dish']]:12s} | volume={case['volume']:.1f}L, ratio={case['ratio']:.1f}, temp_in={case['temp_in']:.1f}°C -> cook_time={time_pred:.2f}min, cook_temp={temp_pred:.2f}°C")

    # Візуалізація функцій приналежності
    mc.volume.view()
    mc.ratio.view()
    mc.temp_in.view()
    mc.cook_time.view()
    mc.cook_temp.view()
    plt.tight_layout()
    plt.show()