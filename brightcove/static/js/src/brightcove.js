/* Javascript for BrightcoveXBlock. */
function BrightcoveXBlock(runtime, element) {
	var player,
    APIModules,
    videoPlayer;

    function onTemplateLoad(experienceID){
     player = brightcove.api.getExperience(experienceID);
     APIModules = brightcove.api.modules.APIModules;
    }

    function onTemplateReady(evt){
     videoPlayer = player.getModule(APIModules.VIDEO_PLAYER);
     videoPlayer.play();
    }

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
        console.log("asfasf");
        brightcove.createExperiences();
    });
}
