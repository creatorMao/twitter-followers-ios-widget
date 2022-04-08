class IosWidget {
    /**
    * 初始化
    * @param arg 外部传递过来的参数
    */
    constructor(arg) {
        this.arg = arg
        this.arg = "122" //TODO DELETE
        this.widgetSize = config.widgetFamily
    }

    //渲染组件
    async render() {
        if (this.widgetSize === 'small') {
            return await this.renderUI()
        } else if (this.widgetSize === 'large') {
            return await this.renderUI()
        } else {
            return await this.renderUI()
        }
    }

    //返回脚本运行时的时间，作为更新时间
    nowTime() {
        let date = new Date()
        return date.toLocaleTimeString('chinese', { hour12: false })
    }

    /**
     * 渲染小组件UI
     * @returns 
     */
    async renderUI() {
        let color = "#1D9BF0"
        let container = new ListWidget()

        if (!this.arg) {
            var tips = container.addText('请在小组件参数处填写twitterid！')
            tips.textColor = new Color(color)
            tips.font = Font.systemFont(14)
            return container
        }

        //标题
        let header = container.addStack()
        header.centerAlignContent()
        let icon = header.addImage(await this.getImage('https://s3.bmp.ovh/imgs/2022/04/04/8bdbff42330cef61.png'))
        icon.imageSize = new Size(15, 15)
        let title = header.addText(" 关注者")
        title.font = Font.systemFont(13)
        title.textColor = new Color(color)
        container.addSpacer(20)

        //粉丝数据
        let data=this.getData();
        var followers = container.addText(data['FOLLOWERS_COUNT'])
        followers.font = Font.systemFont(32)
        followers.centerAlignText()
        followers.textColor = new Color(color)
        container.addSpacer(20)

        //更新数据
        let updateText = container.addText('更新于:' + this.nowTime())
        updateText.font = Font.systemFont(10)
        updateText.centerAlignText()
        updateText.textColor = new Color(color)
        updateText.textOpacity = 0.5

        return container
    }
    //加载下载数据
    async getData(end, start) {
        let api = '/twitter/followers/latest'
        let req = new Request(api)
        let res = await req.loadJSON()
        //console.log(res)
        return res
    }
    //加载远程图片
    async getImage(url) {
        let req = new Request(url)
        return await req.loadImage()
    }
    //编辑测试使用
    async test() {
        if (config.runsInWidget) return

        this.widgetSize = 'small'
        let w1 = await this.render()
        await w1.presentSmall()

        this.widgetSize = 'medium'
        let w2 = await this.render()
        //await w2.presentMedium()

        this.widgetSize = 'large'
        let w3 = await this.render()
        //await w3.presentLarge()
    }
    //组件单独在桌面运行时调用
    async init() {
        if (!config.runsInWidget) return
        let widget = await this.render()
        Script.setWidget(widget)
        Script.complete()
    }
}
module.exports = IosWidget

// 如果是在编辑器内编辑、运行、测试，则取消注释这行，便于调试：
await new IosWidget().test()
// 如果是组件单独使用（桌面配置选择这个组件使用，则取消注释这一行：
await new IosWidget(args.widgetParameter).init()