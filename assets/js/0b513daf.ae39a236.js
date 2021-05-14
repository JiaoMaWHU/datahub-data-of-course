(self.webpackChunkdocs_website=self.webpackChunkdocs_website||[]).push([[4780],{3905:function(e,t,a){"use strict";a.d(t,{Zo:function(){return l},kt:function(){return p}});var n=a(7294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var u=n.createContext({}),c=function(e){var t=n.useContext(u),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},l=function(e){var t=c(e.components);return n.createElement(u.Provider,{value:t},e.children)},m={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},b=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,o=e.originalType,u=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),b=c(a),p=r,d=b["".concat(u,".").concat(p)]||b[p]||m[p]||o;return a?n.createElement(d,i(i({ref:t},l),{},{components:a})):n.createElement(d,i({ref:t},l))}));function p(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=a.length,i=new Array(o);i[0]=b;var s={};for(var u in t)hasOwnProperty.call(t,u)&&(s[u]=t[u]);s.originalType=e,s.mdxType="string"==typeof e?e:r,i[1]=s;for(var c=2;c<o;c++)i[c]=a[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}b.displayName="MDXCreateElement"},3195:function(e,t,a){"use strict";a.r(t),a.d(t,{frontMatter:function(){return i},metadata:function(){return s},toc:function(){return u},default:function(){return l}});var n=a(2122),r=a(9756),o=(a(7294),a(3905)),i={title:"MXE Processing Jobs",hide_title:!0,slug:"/metadata-jobs",custom_edit_url:"https://github.com/linkedin/datahub/blob/master/metadata-jobs/README.md"},s={unversionedId:"metadata-jobs/README",id:"metadata-jobs/README",isDocsHomePage:!1,title:"MXE Processing Jobs",description:"DataHub uses Kafka as the pub-sub message queue in the backend. There are 2 Kafka topics used by DataHub which are",source:"@site/genDocs/metadata-jobs/README.md",sourceDirName:"metadata-jobs",slug:"/metadata-jobs",permalink:"/docs/metadata-jobs",editUrl:"https://github.com/linkedin/datahub/blob/master/metadata-jobs/README.md",version:"current",frontMatter:{title:"MXE Processing Jobs",hide_title:!0,slug:"/metadata-jobs",custom_edit_url:"https://github.com/linkedin/datahub/blob/master/metadata-jobs/README.md"}},u=[],c={toc:u};function l(e){var t=e.components,a=(0,r.Z)(e,["components"]);return(0,o.kt)("wrapper",(0,n.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("p",null,"DataHub uses Kafka as the pub-sub message queue in the backend. There are 2 Kafka topics used by DataHub which are\n",(0,o.kt)("inlineCode",{parentName:"p"},"MetadataChangeEvent")," and ",(0,o.kt)("inlineCode",{parentName:"p"},"MetadataAuditEvent"),"."),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("inlineCode",{parentName:"li"},"MetadataChangeEvent:")," This message is emitted by any data platform or crawler in which there is a change in the metadata."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("inlineCode",{parentName:"li"},"MetadataAuditEvent:")," This message is emitted by ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/linkedin/datahub/blob/master/gms"},"DataHub GMS")," to notify that metadata change is registered.")),(0,o.kt)("p",null,"To be able to consume from these two topics, there are two ",(0,o.kt)("a",{parentName:"p",href:"https://kafka.apache.org/documentation/streams/"},"Kafka Streams"),"\njobs DataHub uses:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("a",{parentName:"li",href:"https://github.com/linkedin/datahub/blob/master/metadata-jobs/mce-consumer-job"},"MCE Consumer Job"),": Writes to ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/linkedin/datahub/blob/master/gms"},"DataHub GMS")),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("a",{parentName:"li",href:"https://github.com/linkedin/datahub/blob/master/metadata-jobs/mae-consumer-job"},"MAE Consumer Job"),": Writes to ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/linkedin/datahub/blob/master/docker/elasticsearch"},"Elasticsearch")," & ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/linkedin/datahub/blob/master/docker/neo4j"},"Neo4j"))))}l.isMDXComponent=!0}}]);