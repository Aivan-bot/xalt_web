export default function (config) {
  config.setUseGitIgnore(false);

  // PASST: D'output-Struktur muess im docs/ Root lige (nid docs/pages/)
  config.addPassthroughCopy({
    "./css": "css",
    "./js": "js",
    "./src/images": "images",
    "./sitemap.xml": "sitemap.xml",
    "./xalt_sitemap.md": "xalt_sitemap.md",
  });

  config.setTemplateFormats("md,njk,html");
  config.addLayoutAlias("base", "layouts/base.njk");
  config.addLayoutAlias("null", "null");

  // Filter: remove 'pages/' prefix from output paths
  config.addFilter("eleventyOutputPath", (path) => {
    // src/pages/foo/index.md → foo/index.html  (no pages/)
    if (path.startsWith("pages/")) {
      return path.replace("pages/", "");
    }
    return path;
  });

  // Shortcodes
  config.addNunjucksShortcode("include", (file) => {
    return file;
  });

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
    pathPrefix: "/",
    htmlTemplateEngine: "njk",
    dataTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: "njk",
    filters: {
      eleventyOutputPath: (path) => {
        if (path && path.startsWith("pages/")) {
          return path.replace("pages/", "");
        }
        return path;
      },
    },
  };
}
