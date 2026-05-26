import { eleventy } from '@11ty/eleventy';

export default function (config) {
  // Passthrough file copy
  config.addPassthroughCopy("./css");
  config.addPassthroughCopy("./js");
  config.addPassthroughCopy("./images/**/*");
  
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
      output: "dist",
      includes: "_includes",
      data: "_data",
    },
    // Use ES modules
    htmlTemplateEngine: "njk",
    dataTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html"],
  };
}
