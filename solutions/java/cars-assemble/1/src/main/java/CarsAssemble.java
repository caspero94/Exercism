public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double prod = 221 * speed;
        if (speed == 10) {
            return prod * 0.77;
        }
        else if (speed == 9) {
            return prod * 0.80;
        }
        else if (speed > 4) {
            return prod * 0.9;
        }
        else {
            return prod;
        }
    }

    public int workingItemsPerMinute(int speed) {
        return (int) productionRatePerHour(speed) / 60;
    }
}
