const path = require('path')
const { VueLoaderPlugin } = require('vue-loader')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const StyleLintPlugin = require('stylelint-webpack-plugin')
const webpack = require('webpack')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')
const WebpackVersionFilePlugin = require('webpack-version-file-plugin')
const execa = require('execa')

require('babel-polyfill')

const repoRoot = __dirname
const appRoot = path.join(repoRoot, 'app')
const distRoot = path.join(repoRoot, 'dist')
const publicRoot = path.join(repoRoot, 'public')


module.exports = (env, argv) => {
    const mode = argv ? argv.mode : 'development'

    let isProd = () => {
        return mode !== 'development'
    }

    const packageJson = require('./package.json')
    const version = JSON.stringify(require('./package.json').version)

    const name = packageJson.name

    let plugins = [
        new VueLoaderPlugin(),
        new VuetifyLoaderPlugin(),
        new HtmlWebpackPlugin({
            title: `${name} ${version}`,
            template: path.join(publicRoot, 'index.html'),
        }),
        new StyleLintPlugin({
            files: ['**/*.{vue,htm,html,css,scss,sass}'],
        }),
        new webpack.DefinePlugin({
            __VERSION__: version,
        }),
    ]

    if (isProd()) {
        const gitHash = execa.sync('git', ['rev-parse', '--short', 'HEAD']).stdout
        const gitNumCommits = Number(execa.sync('git', ['rev-list', 'HEAD', '--count']).stdout)
        const gitDirty = execa.sync('git', ['status', '-s', '-uall']).stdout.length > 0
        plugins = [
            ...plugins,
            new WebpackVersionFilePlugin({
                packageFile: path.join(__dirname, 'package.json'),
                template: path.join(__dirname, 'version.ejs'),
                outputFile: path.join('app/', 'version.json'),
                extras: {
                    githash: gitHash,
                    gitNumCommits: gitNumCommits,
                    timestamp: Date.now(),
                    dirty: gitDirty,
                },
            }),
            new CopyWebpackPlugin([{
                from: path.join(publicRoot, 'assets'),
                to: 'public/assets',
            }]),
        ]
    }

    return {
        context: appRoot,

        output: {
            path: distRoot,
            filename: '[name].[hash].js',
            chunkFilename: '[name].[chunkhash].js',
            publicPath: '/',
        },

        plugins: plugins,

        entry: {
            index: ['babel-polyfill', path.join(appRoot, 'index.js')],
            vendor: [
                'vue',
                'vuex',
                'axios',
                'lodash/template',
                'lodash/orderBy',
                'vue-router',
                'humps',
            ],
        },
        resolve: {
            modules: [
                appRoot,
                'node_modules',
            ],
            extensions: ['*', '.js', '.vue', '.json'],
        },
        optimization: {
            splitChunks: {
                cacheGroups: {
                    vendor: {
                        chunks: 'initial',
                        name: 'vendor',
                        test: 'vendor',
                        enforce: true,
                    },
                },
            },
            runtimeChunk: true,
        },
        module: {
            rules: [
                {
                    test: /\.(woff|woff2|ttf|eot)$/,
                    use: 'file-loader?name=fonts/[name].[ext]!static',
                },
                {
                    test: /\.(js|vue)$/,
                    use: 'eslint-loader',
                    exclude: /node_modules/,
                    enforce: 'pre',
                },
                {
                    test: /\.js$/,
                    use: 'babel-loader',
                    include: [appRoot],
                },
                {
                    test: /\.vue$/,
                    loader: 'vue-loader',
                    options: {
                        compilerOptions: {
                            modules: [VuetifyLoaderPlugin],
                        },
                    },
                },
                {
                    test: /\.svg$/,
                    use: 'file-loader',
                },
                {
                    test: /\.(png|jpg|jpeg|gif|svg)(\?.*)?$/,
                    use: [
                        'url-loader?name=assets/[name].[ext]',
                    ],
                },
                {
                    test: /\.(sa|sc|c)ss$/,
                    use: [
                        'vue-style-loader',
                        'css-loader',
                        'postcss-loader',
                        {
                            loader: 'sass-loader',
                            options: {
                                implementation: require('sass'),
                            },
                        },
                    ],
                },
                {
                    test: /\.styl$/,
                    use: [
                        'style-loader',
                        'css-loader',
                        {
                            loader: 'stylus-loader',
                            options: {
                            },
                        },
                    ],
                },
            ],
        },
        devtool: isProd() ? false : '#eval-source-map',
        devServer: {
            host: '0.0.0.0',
            port: '9040',
            disableHostCheck: true,
            historyApiFallback: true,
            watchOptions: {
                poll: true,
            },
        },
    }
}
