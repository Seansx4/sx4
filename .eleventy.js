module.exports = function(eleventyConfig){

    eleventyConfig.addPassthroughCopy('./src/css');
    eleventyConfig.addPassthroughCopy('./src/images');
    eleventyConfig.addPassthroughCopy('./src/js');
    eleventyConfig.addPassthroughCopy('./src/python');
    eleventyConfig.addPassthroughCopy('./src/robots.txt');
    
    // Sitemap whitespace config
    eleventyConfig.addTransform("xmlWhitespaceFix", function (content, outputPath) {
    if (outputPath && outputPath.endsWith("sitemap.xml")) {
        return content.trim();
    }
    return content;
    });



    return{
        dir: {
            input:"src",
            output: "public"
        }
    };
}