document.addEventListener("DOMContentLoaded", function () {
    const content = document.querySelector(".rst-content");

    if (!content || document.querySelector(".doc-comments")) {
        return;
    }

    const comments = document.createElement("section");
    comments.className = "doc-comments";

    const title = document.createElement("h2");
    title.textContent = "评论与反馈";
    comments.appendChild(title);

    const script = document.createElement("script");
    script.src = "https://giscus.app/client.js";

    // 替换成 giscus.app 生成的真实参数
    script.setAttribute("data-repo", "Penguin-77/MiniCabLite-Manual");
    script.setAttribute("data-repo-id", "R_kgDOTufHjg");
    script.setAttribute("data-category", "Announcements");
    script.setAttribute("data-category-id", "DIC_kwDOTufHjs4DCttU");

    script.setAttribute("data-mapping", "pathname");
    script.setAttribute("data-strict", "0");
    script.setAttribute("data-reactions-enabled", "1");
    script.setAttribute("data-emit-metadata", "0");
    script.setAttribute("data-input-position", "top");
    script.setAttribute("data-theme", "light");
    script.setAttribute("data-lang", "zh-CN");
    script.setAttribute("data-loading", "lazy");

    script.crossOrigin = "anonymous";
    script.async = true;

    comments.appendChild(script);
    content.appendChild(comments);
});