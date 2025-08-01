/**
 * OverlayScrollbars adapter.
 * https://kingsora.github.io/OverlayScrollbars/
 */
ckan.module("likes-scrollbar", function ($) {
  return {
    options: {},

    initialize() {
      // stop execution if dependency is missing.
      if (typeof OverlayScrollbarsGlobal === "undefined") {
        // reporting the source of the problem is always a good idea.
        console.error(
          "[likes-scrollbar] OverlayScrollbars library is not loaded",
        );
        return;
      }

      const options = this.sandbox["likes"].nestedOptions(
        this.options,
      );

      OverlayScrollbarsGlobal.OverlayScrollbars(this.el[0], options)
    },
  };
});
