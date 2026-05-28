export default function (config) {
  // Only read from src directory - ignore everything else
  config.setUseGitIgnore(false);
  
  // Passthrough file copy
  config.addPassthroughCopy({
    "./css": "css",
    "./js": "js",
    "./images": "images",
    "./sitemap.xml": "sitemap.xml",
    "./xalt_sitemap.md": "xalt_sitemap.md",
  });
  
  // Template engine
  config.setTemplateFormats("md,njk,html");

  // Layout aliases
  config.addLayoutAlias("base", "layouts/base.njk");

  // Shortcodes
  config.addNunjucksShortcode("include", (file) => {
    return file;
  });

  // Filters
  config.addFilter("readtime", (str) => {
    const words = str.split(" ").length;
    return Math.ceil(words / 200);
  });

  return {
    dir: {
      input: "src",
      output: "docs",
      includes: "_includes",
      data: "_data",
    },
    // Ignore all .md except in src/
    pathPrefix: "/",
    // Use ES modules
    htmlTemplateEngine: "njk",
    dataTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: 'njk',
  };
}
