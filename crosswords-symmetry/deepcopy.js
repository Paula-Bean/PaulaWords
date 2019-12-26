
function deepcopy(object) { // Adapted from https://stackoverflow.com/a/39029912
    const cache = new WeakMap();

    function recursivecopy(obj) {
        if (typeof obj !== 'object' || obj === null)
            return obj; // primitive value

        if (obj instanceof Set)
            return new Set(obj);

        // Examples of other data types you might need to handle:
        // if (obj instanceof Date) return new Date().setTime(obj.getTime());
        // if (obj instanceof RegExp) return new RegExp(obj.source, obj.flags);

        if (cache.has(obj))
            return cache.get(obj);

        const result = obj instanceof Array ? [] : {};
        cache.set(obj, result);
        if (obj instanceof Array) {
            for (const o of obj) {
                result.push(recursivecopy(o));
                }
            return result;
            }

        const keys = Object.keys(obj);
        for (const key of keys)
            result[key] = recursivecopy(obj[key]);

        return result;
        }

    return recursivecopy(object);
}
