public class Lasagna {
    public int expectedMinutesInOven(){
        return 40;
    }

    public int remainingMinutesInOven(int timehot){
        return expectedMinutesInOven() - timehot;
    }

    public int preparationTimeInMinutes(int layers){
        return 2 * layers;
    }
    public int totalTimeInMinutes(int layers, int timehot){
        return preparationTimeInMinutes(layers) + timehot;
    }
}
