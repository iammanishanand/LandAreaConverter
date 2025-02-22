class LandConverter:
    CONVERSION_TABLE = {
        "marla": 272.25,
        "sarsai": 30.25,
        "kanal": 5445,
        "bigha": 9072,
        "biswa": 455.4,
        "killa": 43560,
        "acre": 43560,
        "square_feet": 1,
        "square_meter": 10.7639,
        "guntha": 1089,
        "square_inch": 0.00694444,
        "hectare": 107639.104,
        "ground": 2400,
        "square_mile": 27878400,
        "square_karam": 30.25,
        "square_kilometer": 10763910.4,
        "murabba": 10890000,
        "decimal": 435.6,
        "lessa": 108.9,
        "cent": 435.6,
        "biswa_kacha": 750,
        "marla_selected": 272.25,
        "chatak": 180,
        "dhur": 68,
        "biswa": 455.4,
        "square_yard": 9,
        "gaj": 9,
        "pura": 1089,
        "katha": 1361.25,
        "square_centimeter": 0.00107639
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in cls.CONVERSION_TABLE or to_unit not in cls.CONVERSION_TABLE:
            raise ValueError("Invalid unit provided. Please use a valid land measurement unit.")
        
        value_in_sqft = value * cls.CONVERSION_TABLE[from_unit]  # Convert to square feet first
        converted_value = value_in_sqft / cls.CONVERSION_TABLE[to_unit]  # Convert to target unit
        
        return converted_value

if __name__ == "__main__":
    print("Welcome to Punjab Land Area Converter!")
    print("Available units: marla, sarsai, kanal, bigha, biswa, killa, acre, square_feet, square_meter, guntha, square_inch, hectare, ground, square_mile, square_karam, square_kilometer, murabba, decimal, lessa, cent, biswa_kacha, marla_selected, chatak, dhur, biswa, square_yard, gaj, pura, katha, square_centimeter")
    
    value = float(input("Enter the land area value: "))
    from_unit = input("Enter the current unit: ")
    to_unit = input("Enter the unit to convert to: ")
    
    try:
        result = LandConverter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
    except ValueError as e:
        print(e)
