public class Lasagna {
    int lasagnaTime = 40;
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven(){
        return lasagnaTime;
    }

    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int timehot){
        return lasagnaTime - timehot;
    }

    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int layers){
        return 2 * layers;
    }
    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int layers, int timehot){
        return preparationTimeInMinutes(layers) + timehot;
    }
}
