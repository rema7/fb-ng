module.exports = {
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
    node: true,
    mocha: true
  },
  globals: {
    expect: true
  },
  extends: [
    'plugin:vue/essential',
    'standard'
  ],
  plugins: [
    'vue'
  ],
  rules: {
    "arrow-parens": ["error", "always"],
    "camelcase": ["error", { "properties": "never" }],
    "comma-dangle": ["error", "always-multiline"],
    "eqeqeq": ["error", "always"],
    "indent": ["error", 4, { "SwitchCase": 1 }],
    "max-len": ["error", 200, { "ignoreStrings": true }],
    "no-duplicate-imports": "error",
    "no-multiple-empty-lines": ["error", { "max": 2, "maxEOF": 1 }],
    "no-multi-spaces": ["error"],
    "quote-props": ["error", "consistent-as-needed"],
    "quotes": ["error", "single"],
    "semi": ["error", "never"],
    "vue/html-indent": ["error", 4, { "alignAttributesVertically": true }]
  },
}
