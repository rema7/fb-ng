import Vue from 'vue'
import Vuex from 'vuex'


import account from 'store/modules/Account'
import auth from 'store/modules/Auth'

import billing from 'store/modules/Billing'

import category from 'store/modules/category/Category'
import categoryLocalizations from 'store/modules/category/CategoryLocalizations'
import categoryPlaylists from 'store/modules/category/CategoryPlaylists'
import categories from 'store/modules/category/Categories'

import dealer from 'store/modules/dealer/Dealer'
import dealerHotels from 'store/modules/dealer/DealerHotels'
import dealerLocations from 'store/modules/dealer/DealerLocations'
import dealers from 'store/modules/dealer/Dealers'

import devices from 'store/modules/device/Devices'

import events from 'store/modules/events/Events'

import firmwares from 'store/modules/firmware/Firmwares'

import hotel from 'store/modules/hotel/Hotel'
import hotelBilling from 'store/modules/hotel/HotelBilling'
import hotelCategories from 'store/modules/hotel/HotelCategories'
import hotelDevices from 'store/modules/hotel/HotelDevices'
import hotelGreetings from 'store/modules/hotel/HotelGreetings'
import hotelPackages from 'store/modules/hotel/HotelPackages'
import hotelPlaylists from 'store/modules/hotel/HotelPlaylists'
import hotelRoom from 'store/modules/room/HotelRoom'
import hotelRoomDevices from 'store/modules/room/HotelRoomDevices'
import hotelRooms from 'store/modules/hotel/HotelRooms'
import hotelUsers from 'store/modules/hotel/HotelUsers'
import hotels from 'store/modules/hotel/Hotels'

import languages from 'store/modules/language/Languages'

import location from 'store/modules/location/Location'
import locationDealers from 'store/modules/location/LocationDealers'
import locationHotels from 'store/modules/location/LocationHotels'
import locationOffers from 'store/modules/location/LocationOffers'
import locations from 'store/modules/location/Locations'

import offers from 'store/modules/offer/Offers'

import pack from 'store/modules/package/Package'
import packageLocalizations from 'store/modules/package/PackageLocalizations'
import packageVideos from 'store/modules/package/PackageVideos'
import packages from 'store/modules/package/Packages'

import playlist from 'store/modules/playlist/Playlist'
import playlistLocalizations from 'store/modules/playlist/PlaylistLocalizations'
import playlistVideos from 'store/modules/playlist/PlaylistVideos'
import playlists from 'store/modules/playlist/Playlists'

import videos from 'store/modules/video/Videos'
import video from 'store/modules/video/Video'
import videoManager from 'store/modules/manager/VideoManager'
import videoManagerCredentials from 'store/modules/manager/VideoManagerCredentials'
import videoLocalizations from 'store/modules/video/VideoLocalizations'
import videoPackages from 'store/modules/video/VideoPackages'
import videoPlaylists from 'store/modules/video/VideoPlaylists'
import videoPosters from 'store/modules/video/VideoPosters'
import videoLocations from 'store/modules/video/VideoLocations'

import settings from 'store/modules/Settings'


Vue.use(Vuex)

const actions = {

}

const state = {
}

const mutations = {
}

const getters = {

}

const modules = {
    account,
    auth,

    settings,
}

export default new Vuex.Store({
    state,
    mutations,
    getters,
    modules,
    actions,
})
