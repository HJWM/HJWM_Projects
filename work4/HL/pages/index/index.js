// example/activity_room/index.js
var info1 = [{
  date: '2018-10-20',
  begin_time: '21:00',
  end_time: '23:00',
  reason: '交流学习',
  name: '张总',
  department: '网媒',
  uid: '1001',
},
{
  date: '2018-10-21',
  begin_time: '22:00',
  end_time: '23:30',
  reason: '开会',
  name: '王姐',
  department: '云计算',
  uid: '1002',
},
{
  date: '2018-10-22',
  begin_time: '19:00',
  end_time: '21:00',
  reason: '开会',
  name: '程总',
  department: '主席团',
  uid: '1003',
}];
wx.setStorage({
  key: 'wm',
  data: info1
}),

Page({
  /**
   * 页面的初始数据
   */
  data: {
    array:[],
    userinfo:{}
  },

  openToast: function (e) {
    var id = parseInt(e.currentTarget.id);
    var re = this.data.array[id];
    wx.showToast({
      title: re.name + " " + re.reason,
      icon: "none",
      mask: true,
      duration: 1500
    });
  },

  addinfo:function() {
    wx.navigateTo({
 //     url: '../index'
      url: 'input_info',
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.getStorage({
      key: 'wm',
      success: res => {
        console.log('成功:',res);
        this.setData({
          array: res.data
        })
      },
      complete: function(res){
        console.log('完成：'+res);
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    console.log(this.data.userinfo)
    wx.getStorage({
      key: 'user',
      success: info => {
        console.log('接受的数据', info)
        this.setData({
          userinfo: info.data
        })
        console.log('--------')
        console.log(this.data.userinfo)
        info1.push(this.data.userinfo)
        wx.setStorage({
          key: 'wm',
          data: info1
        })
        wx.getStorage({
          key: 'wm',
          success: res => {
            console.log('成功:', res);
            this.setData({
              array: res.data
            })
          },
          complete: function (res) {
            console.log('完成：' + res);
          }
        })
      },
    })
//    this.data.user = wx.getStorageSync('user'),
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})