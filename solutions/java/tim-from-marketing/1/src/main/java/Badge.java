class Badge {
    public String print(Integer id, String name, String department) {
        String res = name;
        
        if (department != null){
            res += " - " + department.toUpperCase(); 
        } else {
            res += " - OWNER";
        }
        if (id != null){
            res = "[" + String.valueOf(id) + "] - " + res;
        }
        return res;
    }
}
