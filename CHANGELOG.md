# Changelog

## 0.5.0 (2026-09-01)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/dedalus-labs/dedalus-python/compare/v0.4.0...v0.5.0)

### ⚠ BREAKING CHANGES

* **api:** regenerate SDKs from the current public DCS contract

### Features

* **api:** regenerate SDKs from the current public DCS contract ([04208ef](https://github.com/dedalus-labs/dedalus-python/commit/04208ef05cb07426d68717abb57835e089b76205))
* **stlc:** configurable CI runner and private-production-repo support in workflow templates ([6acb1d3](https://github.com/dedalus-labs/dedalus-python/commit/6acb1d303d2a07cf6c01f63005a4f98541c47f40))


### Bug Fixes

* **auth:** prioritize first auth header ([81f3c28](https://github.com/dedalus-labs/dedalus-python/commit/81f3c288b2ae2e97046344177500714e1e4ce6be))
* **internal:** resolve build failures ([c10ce00](https://github.com/dedalus-labs/dedalus-python/commit/c10ce00180c146772ec9f390e3d058a1d9462082))


### Chores

* **internal:** allow the mock server port to be set with STAINLESS_MOCK_PORT ([aa8a0ee](https://github.com/dedalus-labs/dedalus-python/commit/aa8a0ee9f29ad6fa93a917baba1ab0ffaebb6959))

## 0.4.0 (2026-05-12)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/dedalus-labs/dedalus-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** add usage endpoints/autosleep ([3ebb476](https://github.com/dedalus-labs/dedalus-python/commit/3ebb476fd66187dce852e6efc8c5ea80d095e0dd))

## 0.3.0 (2026-05-12)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/dedalus-labs/dedalus-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** add orgs usage endpoints, autosleep to machines, remove if_match parameters ([3ecc5f7](https://github.com/dedalus-labs/dedalus-python/commit/3ecc5f71350a236eeb38b6ca1116146378ea7f20))
* **internal/types:** support eagerly validating pydantic iterators ([d2686f3](https://github.com/dedalus-labs/dedalus-python/commit/d2686f3ea4d92a9b4c1ab211f62483dd2cdfc712))
* support setting headers via env ([31654ea](https://github.com/dedalus-labs/dedalus-python/commit/31654ea7dba81fd19b0c334846eb4bf988035224))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([aa1c869](https://github.com/dedalus-labs/dedalus-python/commit/aa1c869547ee96d99910ac50f0962c02812cf844))
* use correct field name format for multipart file arrays ([09bc433](https://github.com/dedalus-labs/dedalus-python/commit/09bc4338396af1f0a28df189bd026ce052554532))


### Chores

* **internal:** reformat pyproject.toml ([6a4934a](https://github.com/dedalus-labs/dedalus-python/commit/6a4934a311b675e0b59dfe5e1d521e2d9405b62f))
* remove custom code ([e296321](https://github.com/dedalus-labs/dedalus-python/commit/e2963215b941cf1f14c44215f4c5ba8427ea00d4))

## 0.2.0 (2026-04-22)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/dedalus-labs/dedalus-python/compare/v0.1.0...v0.2.0)

### Features

* **client:** add event handler implementation for websockets ([d46b70f](https://github.com/dedalus-labs/dedalus-python/commit/d46b70f7330c7441113cc3aa3cb61b41880c2894))
* **client:** add path parameters for web sockets ([a805582](https://github.com/dedalus-labs/dedalus-python/commit/a8055824a4bf357d1e8394f02995eb9811df4b18))
* **client:** allow enqueuing to websockets even when not connected ([3c790cf](https://github.com/dedalus-labs/dedalus-python/commit/3c790cf35c3a28645cf65b2fa199fceb53677990))
* **client:** support reconnection in websockets ([e5e6c38](https://github.com/dedalus-labs/dedalus-python/commit/e5e6c38b62bf19f8d85538555251650f6ab1dd91))
* **client:** support sending raw data over websockets ([235869c](https://github.com/dedalus-labs/dedalus-python/commit/235869ccaad5bd8d9c7cffc82df7902b2e324205))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([9d1b3a5](https://github.com/dedalus-labs/dedalus-python/commit/9d1b3a5b6c3a44600ea52faa57188fc7c8b6a56c))
* ensure file data are only sent as 1 parameter ([41853cb](https://github.com/dedalus-labs/dedalus-python/commit/41853cbc3978376af90de18138b9aaa6518a8c28))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([f1a1920](https://github.com/dedalus-labs/dedalus-python/commit/f1a1920db2ae8618db678ca4a48ed4bac1c07c4a))


### Chores

* **ci:** remove release-doctor workflow ([20dab67](https://github.com/dedalus-labs/dedalus-python/commit/20dab671a0fef62c936a1fd1c23c71ece9101b31))
* **internal:** codegen related update ([126141f](https://github.com/dedalus-labs/dedalus-python/commit/126141f2387570bbff3e841a011a5ccd4e75e1ae))
* **internal:** more robust bootstrap script ([7aa05e9](https://github.com/dedalus-labs/dedalus-python/commit/7aa05e9b067a3db4475e95ababd9f39730d080ea))
* remove custom code ([84a40a9](https://github.com/dedalus-labs/dedalus-python/commit/84a40a90c844ce8029fb1a67bd9b6d922ab954ba))
* **tests:** bump steady to v0.22.1 ([b1e0be9](https://github.com/dedalus-labs/dedalus-python/commit/b1e0be98f18c4d06c5f46abaf3c3491b875ad7da))

## 0.1.0 (2026-04-02)

Full Changelog: [v0.0.4...v0.1.0](https://github.com/dedalus-labs/dedalus-python/compare/v0.0.4...v0.1.0)

### Features

* **api:** add sleep & wake methods ([e9709ab](https://github.com/dedalus-labs/dedalus-python/commit/e9709abd85042a51ca1fab6bc4270e3b0ddbe602))

## 0.0.4 (2026-04-01)

Full Changelog: [v0.0.3...v0.0.4](https://github.com/dedalus-labs/dedalus-python/compare/v0.0.3...v0.0.4)

### Features

* **internal:** implement indices array format for query and form serialization ([964fbdf](https://github.com/dedalus-labs/dedalus-python/commit/964fbdfd66a57ce61c8db07cca40032c877a20ed))


### Chores

* **api:** rename workspaces to machines ([ebbdaee](https://github.com/dedalus-labs/dedalus-python/commit/ebbdaeefd99fb507499f2d9ec5c68f258ccc900e))
* **tests:** bump steady to v0.20.1 ([fe9a91b](https://github.com/dedalus-labs/dedalus-python/commit/fe9a91b905ce79bd75487c4d1ad7b7e027d1c99e))
* **tests:** bump steady to v0.20.2 ([e4097a4](https://github.com/dedalus-labs/dedalus-python/commit/e4097a4700e2ccc894504a796e5fa8511d36eacb))

## 0.0.3 (2026-03-25)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/dedalus-labs/dedalus-python/compare/v0.0.2...v0.0.3)

### Bug Fixes

* **api:** rename stream_status to watch, remove wake_if_needed from workspace methods ([453d5c3](https://github.com/dedalus-labs/dedalus-python/commit/453d5c37afde54a6b1603b2485b0100f894acfd1))
* sync uv.lock version with pyproject.toml ([45e2a3f](https://github.com/dedalus-labs/dedalus-python/commit/45e2a3fbb28cc4a3f4d8183827ec17d46113ee3e))


### Chores

* **ci:** skip lint on metadata-only changes ([d38d11a](https://github.com/dedalus-labs/dedalus-python/commit/d38d11a241f8b47dcf62ecb2933f72f70e80aca4))
* **tests:** bump steady to v0.19.7 ([ea163fc](https://github.com/dedalus-labs/dedalus-python/commit/ea163fc51951aca7687bbb7936113c1432df3a2e))

## 0.0.2 (2026-03-23)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/dedalus-labs/dedalus-python/compare/v0.0.1...v0.0.2)

### Bug Fixes

* **api:** add stream_status SSE endpoint, websocket terminals, websocket_base_url param ([b377c15](https://github.com/dedalus-labs/dedalus-python/commit/b377c15509fd024a3a26d24907ddb1a6426eca79))
* sanitize endpoint path params ([ddb7735](https://github.com/dedalus-labs/dedalus-python/commit/ddb7735faa56c28c05775dc625f2db7fede23c7c))


### Chores

* **internal:** update gitignore ([54dd954](https://github.com/dedalus-labs/dedalus-python/commit/54dd954d904154caa3ba532a22c08c809d840676))
* **tests:** bump steady to v0.19.4 ([c6813af](https://github.com/dedalus-labs/dedalus-python/commit/c6813af7f4f6c8995ca644160b30aac303160bee))
* **tests:** bump steady to v0.19.5 ([6b3f3df](https://github.com/dedalus-labs/dedalus-python/commit/6b3f3dff25d9416ebd57e1be69cbb6b94747018f))
* **tests:** bump steady to v0.19.6 ([7e6cdf9](https://github.com/dedalus-labs/dedalus-python/commit/7e6cdf9d37fd9f5bddaea9c707534c3b2ceab0e5))


### Refactors

* **tests:** switch from prism to steady ([1766adf](https://github.com/dedalus-labs/dedalus-python/commit/1766adfac04d3544abff0e45830865dca9fbec38))

## 0.0.1 (2026-03-18)

Full Changelog: [v0.0.1...v0.0.1](https://github.com/dedalus-labs/dedalus-python/compare/v0.0.1...v0.0.1)

### Bug Fixes

* **api:** consolidate pagination & disable websockets ([f5c935c](https://github.com/dedalus-labs/dedalus-python/commit/f5c935c4c01861bd455825cde5b3aa0c7ed36765))


### Chores

* **api:** update homebrew tap and code samples ([8efa47d](https://github.com/dedalus-labs/dedalus-python/commit/8efa47d77d66dc5aa692b05fb92131e87100b397))

## 0.0.1 (2026-03-18)

Full Changelog: [v0.0.1...v0.0.1](https://github.com/dedalus-labs/dedalus-python/compare/v0.0.1...v0.0.1)

### Features

* **api:** stable beta ([e6391a9](https://github.com/dedalus-labs/dedalus-python/commit/e6391a959ccc51ad1f9c5072e2190ea7bfb5a94a))


### Bug Fixes

* **api:** update flags ([21bb2b7](https://github.com/dedalus-labs/dedalus-python/commit/21bb2b79a38d89d4cd092ab2d3f6a70800fbc679))
* **deps:** bump minimum typing-extensions version ([7016283](https://github.com/dedalus-labs/dedalus-python/commit/7016283a4a8b4278321f56b30fec1d5b39bda19e))
* **pydantic:** do not pass `by_alias` unless set ([113574f](https://github.com/dedalus-labs/dedalus-python/commit/113574f4a1f50ea676188724b48497b5491afb5d))


### Chores

* **api:** resolving merge conflicts ([706fa9e](https://github.com/dedalus-labs/dedalus-python/commit/706fa9e077164a8e7a4159e5aa536434ac7e6550))
* **ci:** skip uploading artifacts on stainless-internal branches ([972c929](https://github.com/dedalus-labs/dedalus-python/commit/972c929aef5d5a2bbd8f6b5b0a2ec3d4902dd3b7))
* configure new SDK language ([15fc048](https://github.com/dedalus-labs/dedalus-python/commit/15fc048d78b703a0a1e3e3b763f6890bdefa2e19))
* **internal:** tweak CI branches ([c8ce919](https://github.com/dedalus-labs/dedalus-python/commit/c8ce919b2190e19a9b429494b1016490acae315d))
* update placeholder string ([b8e57a4](https://github.com/dedalus-labs/dedalus-python/commit/b8e57a48d562d50b003121ffe8ecb3bfe9182035))
* update SDK settings ([01a998a](https://github.com/dedalus-labs/dedalus-python/commit/01a998a38e06160aed0acfb53a6b13388fc64761))
* update SDK settings ([b7e80bb](https://github.com/dedalus-labs/dedalus-python/commit/b7e80bb8af98797576d31f5b218fdd2bdf417cd7))
* update SDK settings ([4ceefe7](https://github.com/dedalus-labs/dedalus-python/commit/4ceefe72c5a920b2a83924bfd662cff81c260f42))
* update SDK settings ([00d1f1a](https://github.com/dedalus-labs/dedalus-python/commit/00d1f1ab5a81bbf4bbe076de7261311f351ee477))
* update SDK settings ([2240862](https://github.com/dedalus-labs/dedalus-python/commit/22408628cfde349577c7830b4fb2326e91f43444))
* update SDK settings ([9580045](https://github.com/dedalus-labs/dedalus-python/commit/958004593a4a1369dd7983af2591ac5e0ca655af))
* update SDK settings ([f9cd760](https://github.com/dedalus-labs/dedalus-python/commit/f9cd760421fd8d06c920e23c12e9c289dab2d81a))
