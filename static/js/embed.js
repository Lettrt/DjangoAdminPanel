! function (e) {
    var t = {};

    function n(i) {
        if (t[i]) return t[i].exports;
        var r = t[i] = {
            i: i,
            l: !1,
            exports: {}
        };
        e[i].call(r.exports, r, r.exports, n);
        r.l = !0;
        return r.exports
    }
    n.m = e;
    n.c = t;
    n.d = function (e, t, i) {
        n.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: i
        })
    };
    n.r = function (e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        });
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    };
    n.t = function (e, t) {
        1 & t && (e = n(e));
        if (8 & t) return e;
        if (4 & t && "object" == typeof e && e && e.__esModule) return e;
        var i = Object.create(null);
        n.r(i);
        Object.defineProperty(i, "default", {
            enumerable: !0,
            value: e
        });
        if (2 & t && "string" != typeof e)
            for (var r in e) n.d(i, r, function (t) {
                return e[t]
            }.bind(null, r));
        return i
    };
    n.n = function (e) {
        var t = e && e.__esModule ? function () {
            return e.default
        } : function () {
            return e
        };
        n.d(t, "a", t);
        return t
    };
    n.o = function (e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    };
    n.p = "//static.hsappstatic.net/content-cwv-embed/static-1.388/";
    n(n.s = 1)
}([function (e, t) {
    e.exports = {
        mode: "compressed",
        staticDomainPrefix: "//static.hsappstatic.net",
        bender: {
            depVersions: {
                "content-cwv-embed": "static-1.388",
                "browserslist-config-hubspot": "static-1.55",
                csstype: "static-1.5",
                "head-dlb": "static-1.368",
                HeadJS: "static-2.323",
                "hoist-non-react-statics": "static-3.9",
                "hs-test-utils": "static-1.1445",
                "hub-http": "static-1.787",
                "hub-http-janus": "static-1.352",
                "hub-http-rxjs": "static-1.324",
                HubStyleTokens: "static-2.4719",
                jasmine: "static-4.58",
                "jasmine-runner": "static-1.194",
                "metrics-js": "static-1.2759",
                msw: "static-1.36",
                quartz: "static-1.407",
                react: "static-7.96",
                "react-dom": "static-7.62",
                "react-redux": "static-7.16",
                redux: "static-4.16",
                "redux-thunk": "static-2.11",
                rxjs: "static-5.10",
                StyleGuideUI: "static-3.337",
                "testing-library": "static-1.62",
                "webpack-env": "static-1.4",
                enviro: "static-4.127",
                "hs-promise-rejection-tracking": "static-1.142",
                PortalIdParser: "static-2.120",
                raven: "static-3.26",
                "raven-hubspot": "static-1.240"
            },
            depPathPrefixes: {
                "content-cwv-embed": "/content-cwv-embed/static-1.388",
                "browserslist-config-hubspot": "/browserslist-config-hubspot/static-1.55",
                csstype: "/csstype/static-1.5",
                "head-dlb": "/head-dlb/static-1.368",
                HeadJS: "/HeadJS/static-2.323",
                "hoist-non-react-statics": "/hoist-non-react-statics/static-3.9",
                "hs-test-utils": "/hs-test-utils/static-1.1445",
                "hub-http": "/hub-http/static-1.787",
                "hub-http-janus": "/hub-http-janus/static-1.352",
                "hub-http-rxjs": "/hub-http-rxjs/static-1.324",
                HubStyleTokens: "/HubStyleTokens/static-2.4719",
                jasmine: "/jasmine/static-4.58",
                "jasmine-runner": "/jasmine-runner/static-1.194",
                "metrics-js": "/metrics-js/static-1.2759",
                msw: "/msw/static-1.36",
                quartz: "/quartz/static-1.407",
                react: "/react/static-7.96",
                "react-dom": "/react-dom/static-7.62",
                "react-redux": "/react-redux/static-7.16",
                redux: "/redux/static-4.16",
                "redux-thunk": "/redux-thunk/static-2.11",
                rxjs: "/rxjs/static-5.10",
                StyleGuideUI: "/StyleGuideUI/static-3.337",
                "testing-library": "/testing-library/static-1.62",
                "webpack-env": "/webpack-env/static-1.4",
                enviro: "/enviro/static-4.127",
                "hs-promise-rejection-tracking": "/hs-promise-rejection-tracking/static-1.142",
                PortalIdParser: "/PortalIdParser/static-2.120",
                raven: "/raven/static-3.26",
                "raven-hubspot": "/raven-hubspot/static-1.240"
            },
            project: "content-cwv-embed",
            staticDomain: "//static.hsappstatic.net",
            staticDomainPrefix: "//static.hsappstatic.net"
        }
    }
}, function (e, t, n) {
    "use strict";
    n.r(t);
    const i = "/_hcms/perf/v2",
        r = window,
        a = Math.pow(2, 31);
    var s = n(0);

    function o() {
        const e = document.getElementById("hs-script-loader");
        return e && "SCRIPT" === e.tagName
    }

    function c() {
        return Array.prototype.slice.apply(document.querySelectorAll('script[data-loader="hs-scriptloader"], script#hs-analytics')).filter(e => e.src).map(e => e.id)
    }

    function d() {
        if (!o()) return {
            usesScriptLoader: !1,
            embedIdsPresent: []
        };
        return {
            usesScriptLoader: !0,
            embedIdsPresent: c()
        }
    }

    function l() {
        const e = navigator,
            t = e.connection || e.mozConnection || e.webkitConnection;
        return t ? {
            type: t.type,
            effectiveType: t.effectiveType,
            downlink: t.downlink,
            rtt: t.rtt
        } : {}
    }
    let u = {};

    function p(e) {
        const t = e.navigationType;
        "navigate" !== t && "reload" !== t || (u[e.name] = e.value)
    }

    function f() {
        const e = u;
        u = {};
        return e
    }

    function m(e, t) {
        return Math.floor(Math.round(e / t) * t)
    }

    function h() {
        return performance.timing.toJSON()
    }

    function v() {
        return performance.getEntriesByType("navigation")[0]
    }

    function g() {
        const e = v();
        return {
            startTime: e.startTime,
            requestStart: e.requestStart,
            responseStart: e.responseStart,
            responseEnd: e.responseEnd,
            domComplete: e.domComplete,
            decodedBodySize: e.decodedBodySize,
            encodedBodySize: e.encodedBodySize
        }
    }

    function y() {
        const e = r.hsVars;
        e || console.warn("Cannot collect HS CMS performance data, hsVars are missing");
        const t = s.bender.depVersions[s.bender.project].replace(/static-/, ""),
            n = "static" === t;
        return {
            url: location.href,
            portal: e.portal_id,
            content: e.page_id,
            group: e.content_group_id,
            ticks: e.ticks,
            renderId: e.render_id,
            embedPackageVersion: n ? void 0 : t
        }
    }

    function b() {
        return Object.assign({}, y(), {
            visibleOnScriptLoad: !1
        })
    }

    function w() {
        const e = Object.assign({}, y(), {
                visibleOnScriptLoad: !0,
                connection: l(),
                timing: h(),
                navTiming: g(),
                scriptLoader: d()
            }),
            {
                width: t,
                height: n
            } = T();
        t && n && (e.viewport = {
            width: t,
            height: n
        });
        if (r.hsVideoApi && "function" == typeof r.hsVideoApi.getPerformanceMetrics) {
            const {
                embedType: t,
                embedVersion: n,
                firstVideoLoadedAt: i,
                firstVideoReadyAt: s,
                firstVideoPlayedAt: o,
                numHsVideos: c,
                numAutoplay: d,
                numInitiallyVisible: l,
                numInteractedWith: u,
                secondsOfVideoPlayed: p
            } = r.hsVideoApi.getPerformanceMetrics();
            if (c > 0) {
                e.hsVideo = {
                    embedType: t,
                    embedVersion: n,
                    numHsVideos: c,
                    numAutoplay: d,
                    numInitiallyVisible: l,
                    numInteractedWith: u,
                    secondsOfVideoPlayed: p
                };
                i && (e.hsVideo.firstVideoLoadedAt = Math.min(i, a));
                s && (e.hsVideo.firstVideoReadyAt = Math.min(s, a));
                o && (e.hsVideo.firstVideoPlayedAt = Math.min(o, a))
            }
        }
        if (r.leadflows && r.leadflows.perfMetrics && "function" == typeof r.leadflows.perfMetrics.getPerformanceMetrics) {
            const {
                numConfigured: t,
                numEmbedsPresent: n,
                numMatchingCurrentUrl: i,
                numRendered: a
            } = r.leadflows.perfMetrics.getPerformanceMetrics();
            t > 0 && (e.leadflows = {
                numConfigured: t,
                numEmbedsPresent: n,
                numMatchingCurrentUrl: i,
                numRendered: a
            })
        }
        return e
    }

    function S() {
        const e = w(),
            t = f();
        t && (e.cwv = t);
        return e
    }

    function T() {
        const e = window.innerWidth,
            t = window.innerHeight;
        return e > 0 && t > 0 ? {
            width: m(e, 25),
            height: m(t, 25)
        } : {}
    }
    let E, L = !1;

    function P(e) {
        const t = new XMLHttpRequest;
        t.open("POST", i, !0);
        t.setRequestHeader("Content-type", "application/json");
        t.onreadystatechange = function () {};
        t.send(JSON.stringify(e));
        L = !0
    }

    // function C(e) {
    //     L = navigator.sendBeacon(i + "?viaBeacon=true", new Blob([JSON.stringify(e)], {
    //         type: "application/json"
    //     }))
    // }

    function I(e) {
        try {
            navigator.sendBeacon ? C(e) : P(e)
        } catch (e) {
            console.warn("Error sending HSCMS perf data", e)
        }
    }

    function j() {
        L || I(S())
    }

    function A() {
        L || I(b())
    }

    function M(e) {
        const t = () => {
            if ("hidden" === document.visibilityState) {
                e();
                removeEventListener("visibilitychange", t, !0)
            }
        };
        addEventListener("visibilitychange", t, !0);
        addEventListener("pagehide", e, {
            capture: !0,
            once: !0
        });
        E = () => {
            removeEventListener("visibilitychange", t, !0);
            removeEventListener("pagehide", e, {
                capture: !0
            })
        }
    }

    function V() {
        M(j)
    }

    function _() {
        M(A)
    }
    let x = -1;
    const k = () => x,
        O = e => {
            addEventListener("pageshow", t => {
                if (t.persisted) {
                    x = t.timeStamp;
                    e(t)
                }
            }, !0)
        },
        B = () => `v3-${Date.now()}-${Math.floor(8999999999999*Math.random())+1e12}`,
        H = () => {
            const e = performance.timing,
                t = performance.navigation.type,
                n = {
                    entryType: "navigation",
                    startTime: 0,
                    type: 2 == t ? "back_forward" : 1 === t ? "reload" : "navigate"
                };
            for (const t in e) "navigationStart" !== t && "toJSON" !== t && (n[t] = Math.max(e[t] - e.navigationStart, 0));
            return n
        },
        F = () => window.__WEB_VITALS_POLYFILL__ ? window.performance && (performance.getEntriesByType && performance.getEntriesByType("navigation")[0] || H()) : window.performance && performance.getEntriesByType && performance.getEntriesByType("navigation")[0],
        R = () => {
            const e = F();
            return e && e.activationStart || 0
        },
        q = (e, t) => {
            const n = F();
            let i = "navigate";
            k() >= 0 ? i = "back-forward-cache" : n && (i = document.prerendering || R() > 0 ? "prerender" : document.wasDiscarded ? "restore" : n.type.replace(/_/g, "-"));
            return {
                name: e,
                value: void 0 === t ? -1 : t,
                rating: "good",
                delta: 0,
                entries: [],
                id: B(),
                navigationType: i
            }
        },
        D = (e, t, n) => {
            try {
                if (PerformanceObserver.supportedEntryTypes.includes(e)) {
                    const i = new PerformanceObserver(e => {
                        Promise.resolve().then(() => {
                            t(e.getEntries())
                        })
                    });
                    i.observe(Object.assign({
                        type: e,
                        buffered: !0
                    }, n || {}));
                    return i
                }
            } catch (e) {}
        },
        z = (e, t) => e > t[1] ? "poor" : e > t[0] ? "needs-improvement" : "good",
        J = (e, t, n, i) => {
            let r, a;
            return s => {
                if (t.value >= 0 && (s || i)) {
                    a = t.value - (r || 0);
                    if (a || void 0 === r) {
                        r = t.value;
                        t.delta = a;
                        t.rating = z(t.value, n);
                        e(t)
                    }
                }
            }
        },
        N = e => {
            requestAnimationFrame(() => requestAnimationFrame(() => e()))
        },
        W = e => {
            const t = t => {
                "pagehide" !== t.type && "hidden" !== document.visibilityState || e(t)
            };
            addEventListener("visibilitychange", t, !0);
            addEventListener("pagehide", t, !0)
        },
        U = e => {
            let t = !1;
            return n => {
                if (!t) {
                    e(n);
                    t = !0
                }
            }
        };
    let G = -1;
    const Y = () => "hidden" !== document.visibilityState || document.prerendering ? 1 / 0 : 0,
        $ = e => {
            if ("hidden" === document.visibilityState && G > -1) {
                G = "visibilitychange" === e.type ? e.timeStamp : 0;
                K()
            }
        },
        X = () => {
            addEventListener("visibilitychange", $, !0);
            addEventListener("prerenderingchange", $, !0)
        },
        K = () => {
            removeEventListener("visibilitychange", $, !0);
            removeEventListener("prerenderingchange", $, !0)
        },
        Q = () => {
            if (G < 0) {
                if (window.__WEB_VITALS_POLYFILL__) {
                    G = window.webVitals.firstHiddenTime;
                    G === 1 / 0 && X()
                } else {
                    G = Y();
                    X()
                }
                O(() => {
                    setTimeout(() => {
                        G = Y();
                        X()
                    }, 0)
                })
            }
            return {
                get firstHiddenTime() {
                    return G
                }
            }
        },
        Z = e => {
            document.prerendering ? addEventListener("prerenderingchange", () => e(), !0) : e()
        },
        ee = (e, t) => {
            t = t || {};
            Z(() => {
                const n = [1800, 3e3],
                    i = Q();
                let r, a = q("FCP");
                const s = D("paint", e => {
                    e.forEach(e => {
                        if ("first-contentful-paint" === e.name) {
                            s.disconnect();
                            if (e.startTime < i.firstHiddenTime) {
                                a.value = Math.max(e.startTime - R(), 0);
                                a.entries.push(e);
                                r(!0)
                            }
                        }
                    })
                });
                if (s) {
                    r = J(e, a, n, t.reportAllChanges);
                    O(i => {
                        a = q("FCP");
                        r = J(e, a, n, t.reportAllChanges);
                        N(() => {
                            a.value = performance.now() - i.timeStamp;
                            r(!0)
                        })
                    })
                }
            })
        },
        te = (e, t) => {
            t = t || {};
            ee(U(() => {
                const n = [.1, .25];
                let i, r = q("CLS", 0),
                    a = 0,
                    s = [];
                const o = e => {
                        e.forEach(e => {
                            if (!e.hadRecentInput) {
                                const t = s[0],
                                    n = s[s.length - 1];
                                if (a && e.startTime - n.startTime < 1e3 && e.startTime - t.startTime < 5e3) {
                                    a += e.value;
                                    s.push(e)
                                } else {
                                    a = e.value;
                                    s = [e]
                                }
                            }
                        });
                        if (a > r.value) {
                            r.value = a;
                            r.entries = s;
                            i()
                        }
                    },
                    c = D("layout-shift", o);
                if (c) {
                    i = J(e, r, n, t.reportAllChanges);
                    W(() => {
                        o(c.takeRecords());
                        i(!0)
                    });
                    O(() => {
                        a = 0;
                        r = q("CLS", 0);
                        i = J(e, r, n, t.reportAllChanges);
                        N(() => i())
                    });
                    setTimeout(i, 0)
                }
            }))
        };
    let ne, ie, re, ae;
    const se = {
            passive: !0,
            capture: !0
        },
        oe = new Date,
        ce = e => {
            ae.push(e);
            ue()
        },
        de = () => {
            ae = [];
            ie = -1;
            ne = null;
            me(addEventListener)
        },
        le = (e, t) => {
            if (!ne) {
                ne = t;
                ie = e;
                re = new Date;
                me(removeEventListener);
                ue()
            }
        },
        ue = () => {
            if (ie >= 0 && ie < re - oe) {
                const e = {
                    entryType: "first-input",
                    name: ne.type,
                    target: ne.target,
                    cancelable: ne.cancelable,
                    startTime: ne.timeStamp,
                    processingStart: ne.timeStamp + ie
                };
                ae.forEach((function (t) {
                    t(e)
                }));
                ae = []
            }
        },
        pe = (e, t) => {
            const n = () => {
                    le(e, t);
                    r()
                },
                i = () => {
                    r()
                },
                r = () => {
                    removeEventListener("pointerup", n, se);
                    removeEventListener("pointercancel", i, se)
                };
            addEventListener("pointerup", n, se);
            addEventListener("pointercancel", i, se)
        },
        fe = e => {
            if (e.cancelable) {
                const t = (e.timeStamp > 1e12 ? new Date : performance.now()) - e.timeStamp;
                "pointerdown" == e.type ? pe(t, e) : le(t, e)
            }
        },
        me = e => {
            ["mousedown", "keydown", "touchstart", "pointerdown"].forEach(t => e(t, fe, se))
        },
        he = (e, t) => {
            t = t || {};
            Z(() => {
                const n = [100, 300],
                    i = Q();
                let r, a = q("FID");
                const s = e => {
                        if (e.startTime < i.firstHiddenTime) {
                            a.value = e.processingStart - e.startTime;
                            a.entries.push(e);
                            r(!0)
                        }
                    },
                    o = e => {
                        e.forEach(s)
                    },
                    c = D("first-input", o);
                r = J(e, a, n, t.reportAllChanges);
                c && W(U(() => {
                    o(c.takeRecords());
                    c.disconnect()
                }));
                if (window.__WEB_VITALS_POLYFILL__) {
                    console.warn('The web-vitals "base+polyfill" build is deprecated. See: https://bit.ly/3aqzsGm');
                    c || window.webVitals.firstInputPolyfill(s);
                    O(() => {
                        a = q("FID");
                        r = J(e, a, n, t.reportAllChanges);
                        window.webVitals.resetFirstInputPolyfill();
                        window.webVitals.firstInputPolyfill(s)
                    })
                } else c && O(() => {
                    a = q("FID");
                    r = J(e, a, n, t.reportAllChanges);
                    de();
                    ce(s)
                })
            })
        };
    let ve = 0,
        ge = 1 / 0,
        ye = 0;
    const be = e => {
        e.forEach(e => {
            if (e.interactionId) {
                ge = Math.min(ge, e.interactionId);
                ye = Math.max(ye, e.interactionId);
                ve = ye ? (ye - ge) / 7 + 1 : 0
            }
        })
    };
    let we;
    const Se = () => we ? ve : performance.interactionCount || 0,
        Te = () => {
            "interactionCount" in performance || we || (we = D("event", be, {
                type: "event",
                buffered: !0,
                durationThreshold: 0
            }))
        };
    let Ee = 0;
    const Le = () => Se() - Ee,
        Pe = 10;
    let Ce = [];
    const Ie = {},
        je = e => {
            const t = Ce[Ce.length - 1],
                n = Ie[e.interactionId];
            if (n || Ce.length < Pe || e.duration > t.latency) {
                if (n) {
                    n.entries.push(e);
                    n.latency = Math.max(n.latency, e.duration)
                } else {
                    const t = {
                        id: e.interactionId,
                        latency: e.duration,
                        entries: [e]
                    };
                    Ie[t.id] = t;
                    Ce.push(t)
                }
                Ce.sort((e, t) => t.latency - e.latency);
                Ce.splice(Pe).forEach(e => {
                    delete Ie[e.id]
                })
            }
        },
        Ae = () => {
            const e = Math.min(Ce.length - 1, Math.floor(Le() / 50));
            return Ce[e]
        },
        Me = (e, t) => {
            t = t || {};
            Z(() => {
                const n = [200, 500];
                Te();
                let i, r = q("INP");
                const a = e => {
                        e.forEach(e => {
                            e.interactionId && je(e);
                            if ("first-input" === e.entryType) {
                                !Ce.some(t => t.entries.some(t => e.duration === t.duration && e.startTime === t.startTime)) && je(e)
                            }
                        });
                        const t = Ae();
                        if (t && t.latency !== r.value) {
                            r.value = t.latency;
                            r.entries = t.entries;
                            i()
                        }
                    },
                    s = D("event", a, {
                        durationThreshold: t.durationThreshold || 40
                    });
                i = J(e, r, n, t.reportAllChanges);
                if (s) {
                    s.observe({
                        type: "first-input",
                        buffered: !0
                    });
                    W(() => {
                        a(s.takeRecords());
                        if (r.value < 0 && Le() > 0) {
                            r.value = 0;
                            r.entries = []
                        }
                        i(!0)
                    });
                    O(() => {
                        Ce = [];
                        Ee = Se();
                        r = q("INP");
                        i = J(e, r, n, t.reportAllChanges)
                    })
                }
            })
        },
        Ve = {},
        _e = (e, t) => {
            t = t || {};
            Z(() => {
                const n = [2500, 4e3],
                    i = Q();
                let r, a = q("LCP");
                const s = e => {
                        const t = e[e.length - 1];
                        if (t) {
                            const e = Math.max(t.startTime - R(), 0);
                            if (e < i.firstHiddenTime) {
                                a.value = e;
                                a.entries = [t];
                                r()
                            }
                        }
                    },
                    o = D("largest-contentful-paint", s);
                if (o) {
                    r = J(e, a, n, t.reportAllChanges);
                    const i = U(() => {
                        if (!Ve[a.id]) {
                            s(o.takeRecords());
                            o.disconnect();
                            Ve[a.id] = !0;
                            r(!0)
                        }
                    });
                    ["keydown", "click"].forEach(e => {
                        addEventListener(e, i, !0)
                    });
                    W(i);
                    O(i => {
                        a = q("LCP");
                        r = J(e, a, n, t.reportAllChanges);
                        N(() => {
                            a.value = performance.now() - i.timeStamp;
                            Ve[a.id] = !0;
                            r(!0)
                        })
                    })
                }
            })
        },
        xe = e => {
            document.prerendering ? Z(() => xe(e)) : "complete" !== document.readyState ? addEventListener("load", () => xe(e), !0) : setTimeout(e, 0)
        },
        ke = (e, t) => {
            t = t || {};
            const n = [800, 1800];
            let i = q("TTFB"),
                r = J(e, i, n, t.reportAllChanges);
            xe(() => {
                const a = F();
                if (a) {
                    const s = a.responseStart;
                    if (s <= 0 || s > performance.now()) return;
                    i.value = Math.max(s - R(), 0);
                    i.entries = [a];
                    r(!0);
                    O(() => {
                        i = q("TTFB", 0);
                        r = J(e, i, n, t.reportAllChanges);
                        r(!0)
                    })
                }
            })
        };

    function Oe() {
        if ("hidden" !== document.visibilityState) {
            te(p, {
                reportAllChanges: !0
            });
            Me(p, {
                reportAllChanges: !0
            });
            he(p);
            ee(p);
            _e(p);
            ke(p);
            V()
        } else _()
    }
    Oe()
}]);