def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    #  {’name’: str, ’power’: int, ’type’: str}
    return sorted(artifacts, key=lambda current: current['power'], reverse=True
                  )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    # {’name’: str, ’power’: int, ’element’: str}
    # filtered = filter(lambda current: current['power'] >= min_power, mages)
    # return [current for current in filtered]
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    # {’name’: str, ’power’: int, ’element’: str}
    maximum = max(mages, key=lambda curr: curr['power'])['power']
    minimum = min(mages, key=lambda curr: curr['power'])['power']
    powers = [i['power'] for i in mages]

    return {'max_power': maximum, 'min_power': minimum, 'avg_power':
            round(sum(powers) / len(powers), 2)}


def main() -> None:
    print("Testing artifact sorter...")

    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'fire'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'air'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)

    name1 = sorted_artifacts[0]['name']
    power1 = sorted_artifacts[0]['power']
    name2 = sorted_artifacts[1]['name']
    power2 = sorted_artifacts[1]['power']
    print(f"{name1} ({power1}) comes before {name2} ({power2})")

    print("\nTesting power_filter")
    filtered_artifacts = power_filter(artifacts, 50)
    for i in range(len(filtered_artifacts)):
        name = filtered_artifacts[i]['name']
        power = filtered_artifacts[i]['power']
        print(f"artifact {i}: name: {name}, power: {power}")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    trans_spells = spell_transformer(spells)
    print(" ".join(trans_spells))

    print("\n Testing mage_stats")
    mages = [
        {'name': 'Ilka', 'power': 92, 'element': 'fire'},
        {'name': 'Ahamohlanov', 'power': 85, 'element': 'air'}
    ]
    stats_mages = mage_stats(mages)
    print(f"max_power: {stats_mages["max_power"]}")
    print(f"min_power: {stats_mages["min_power"]}")
    print(f"avg_power: {stats_mages["avg_power"]}")


if __name__ == "__main__":
    main()
