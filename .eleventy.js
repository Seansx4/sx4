module.exports = function(eleventyConfig){

    eleventyConfig.addPassthroughCopy('./src/css');
    eleventyConfig.addPassthroughCopy('./src/images');
    eleventyConfig.addPassthroughCopy('./src/js');
    eleventyConfig.addPassthroughCopy('./src/python');

    return{
        dir: {
            input:"src",
            output: "public"
        }
    };
}