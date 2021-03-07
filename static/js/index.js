$("main").addClass("pre-enter").removeClass("with-hover");
setTimeout(function(){
	$("main").addClass("on-enter");
}, 500);
setTimeout(function(){
	$("main").removeClass("pre-enter on-enter");
	setTimeout(function(){
		$("main").addClass("with-hover");
	}, 50);
}, 2000);

$(".flip, .back a").click(function(){
	$(".player").toggleClass("playlist");
	var id=$(this).data("id");//find("img").attr("src");
	var title=$(this).find("h3").text();
	console.log(src);
	var src="https://www.youtube.com/embed/"+id;
	$("#playerWindow").attr("src", src);
	$("#songTitle").text(title);
});

$(".bottom a").not(".flip").click(function(){
	$(this).toggleClass("active");
});