class SqueakyClean {
    static String clean(String identifier) {
        identifier = identifier.replace(" ", "_").replace("4","a").replace("3","e").replace("0","o").replace("1","l").replace("7","t");
        if (identifier.contains("-")){
        identifier = identifier.substring(0, identifier.indexOf("-")) + identifier.substring(identifier.indexOf("-")+1,identifier.indexOf("-")+2).toUpperCase() + identifier.substring(identifier.indexOf("-")+2,identifier.length());
        }
        identifier = identifier.replaceAll("[^a-zA-Z\\s_]", "");
        return identifier;
    }
}