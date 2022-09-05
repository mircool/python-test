const CryptoJS = require('crypto-js')

function encryptJumpPage(t) {
    if (!t)
        throw "ERROR: 未传入配置项（Object）";
    if (!t.nextPath || !t.query)
        throw "ERROR: 使用加密方法时必须传入属性：".concat(t.nextPath ? "query（需要加密的数据）" : "nextPath（跳转路由地址）");
    if (t.isMatchingPattern) {
        var n = "string" == typeof t.query ? t.query : JSON.stringify(t.query);
        t.newWindow ? d(t.nextPath + "/" + c(n)) : s.b[t.pattern || "push"](t.nextPath + "/" + c(n))
    } else {
        var e, a = {};
        for (e in t.query)
            "string" != typeof t.query[e] && (t.query[e] = String(t.query[e])),
                a[e] = c(t.query[e]);
        t.newWindow ? d(t.nextPath, a) : s.b[t.pattern || "push"]({
            path: t.nextPath,
            query: a
        })
    }
}

const o = {
    keyHex: CryptoJS.enc.Utf8.parse(Object({
        NODE_ENV: "production",
        VUE_APP_BASE_API: "/pro-api",
        VUE_APP_CONSTRUCTION_API: "/pro-api-construction",
        VUE_APP_DEV_FILE_PREVIEW: "/lyjcdFileView/onlinePreview",
        VUE_APP_FILE_ALL_PATH: "http://www.lyjcd.cn:8089",
        VUE_APP_FILE_PREFIX: "/mygroup",
        VUE_APP_LAND_API: "/pro-api-land",
        VUE_APP_PREVIEW_PREFIX: "/lyjcdFileView",
        VUE_APP_PROCUREMENT_API: "/pro-api-procurement",
        VUE_APP_WINDOW_TITLE: "金昌市公共资源交易网",
        BASE_URL: "/"
    }).VUE_APP_CUSTOM_KEY || "54367819"),
    ivHex: CryptoJS.enc.Utf8.parse(Object({
        NODE_ENV: "production",
        VUE_APP_BASE_API: "/pro-api",
        VUE_APP_CONSTRUCTION_API: "/pro-api-construction",
        VUE_APP_DEV_FILE_PREVIEW: "/lyjcdFileView/onlinePreview",
        VUE_APP_FILE_ALL_PATH: "http://www.lyjcd.cn:8089",
        VUE_APP_FILE_PREFIX: "/mygroup",
        VUE_APP_LAND_API: "/pro-api-land",
        VUE_APP_PREVIEW_PREFIX: "/lyjcdFileView",
        VUE_APP_PROCUREMENT_API: "/pro-api-procurement",
        VUE_APP_WINDOW_TITLE: "金昌市公共资源交易网",
        BASE_URL: "/"
    }).VUE_APP_CUSTOM_IV || "54367819")
}

function c(t) {
    return CryptoJS.DES.encrypt(t, o.keyHex, {
        iv: o.ivHex,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).ciphertext.toString()
}


console.log(c('ZBGG'))