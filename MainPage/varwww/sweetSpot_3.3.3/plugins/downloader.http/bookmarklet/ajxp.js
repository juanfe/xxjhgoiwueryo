/*
 * Copyright 2007-2011 Charles du Jeu <contact (at) cdujeu.me>
 * This file is part of AjaXplorer.
 *
 * AjaXplorer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * AjaXplorer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with AjaXplorer.  If not, see <http://www.gnu.org/licenses/>.
 *
 * The latest code can be found at <http://www.ajaxplorer.info/>.
 */
var currentLink;
function parseLinks(){	
	jQuery('body').append('<link rel="stylesheet" type="text/css" href="'+ajxp_bm_target+'plugins/downloader.http/bookmarklet/ajxp.css"></link>');
	jQuery('body').append('<div id="ajxp_bm_main" class="ajxp_bm_menu" ><div><a id="ajxp_bm_close" style="float:right;font-size:12px;cursor:pointer;border-left:1px solid #fff;padding-left: 10px;">X</a>AjaXplorer direct download active</div><div style="color: #ccc; font-size: 10px;	padding: 5px 0px;">Click on any link or image to send the link directly to your AjaXplorer account.<br><input type="checkbox" id="ajxp_dl_now" checked>Trigger download directly</div><div style="display:none" id="ajxp_bm_frame_div"><iframe frameborder="0" id="ajxp_bm_iframe"></iframe></div></div><div style="position:absolute;" class="ajxp_bm_menu" id="ajxp_bm_link_menu"><div id="ajxp_bm_link_title"></div><a id="ajxp_bm_link_dl1">Download to AjaXplorer</a><a id="ajxp_bm_link_dl2">Process link normally</a></div>').click(function(){jQuery('#ajxp_bm_link_menu').slideUp();}) ;
	jQuery(window).bind('scroll', function(){
		jQuery('#ajxp_bm_main').css('top', jQuery(window).scrollTop() + 5);		
	});
	jQuery('#ajxp_bm_main').css('top', jQuery(window).scrollTop() + 5);
	jQuery('#ajxp_bm_link_menu a').hover(
			function(el){jQuery(this).css('color','#ee9');}, 
			function(el){jQuery(this).css('color','#fff');}
		);
	jQuery('#ajxp_bm_link_dl1').click(triggerAjxpDL);
	jQuery('#ajxp_bm_link_dl2').click(triggerOriginalDL);
	var linkHandler = function(event){
		event.preventDefault();
		event.stopPropagation();
		currentLink = jQuery(this);
		var offset = currentLink.offset();
		var height = currentLink.height();
		var href = currentLink.attr("href") || currentLink.attr('src');
		var title = realHref(href);
		jQuery('#ajxp_bm_link_dl2').show();
		if(currentLink.attr("src")){
			if(!currentLink.parents('a').size()){
				jQuery('#ajxp_bm_link_dl2').hide();
			}
		}
		if(title.length > 38){
			title = title.substring(0,10)+'...'+title.substring(title.length-28);
		}		
		jQuery("#ajxp_bm_link_title").html(title).attr("title", realHref(href));
		if(jQuery("#ajxp_bm_link_menu").css('display') == 'none'){
			jQuery("#ajxp_bm_link_menu").css('top', offset.top+height).css('left',offset.left).slideDown();			
		}else{
			jQuery("#ajxp_bm_link_menu").animate({top:offset.top+height,left:offset.left});
		}		
	}; 
	var eachFuncAttacher = function(index){
		var link = jQuery(this);		
		var href = link.attr("href") || link.attr('src');
		if(!href) return;
		link.bind('click', linkHandler).attr('ajxp_bound', 'true');
	};
	jQuery('a,img').each(eachFuncAttacher);
	jQuery('#ajxp_bm_close').click(function(){
		jQuery('a,img').each(function(index){
			var link = jQuery(this);
			if(link.attr('ajxp_bound')){
				link.unbind('click', linkHandler);				
			}
		});
		jQuery('#ajxp_bm_main').remove();
		jQuery('#ajxp_bm_link_menu').remove();
	});	
}
function triggerAjxpDL(){
	jQuery("#ajxp_bm_link_menu").slideUp();
	jQuery('#ajxp_bm_frame_div').slideDown();
	var href = currentLink.attr("href") || currentLink.attr('src');	
	var params = [
		'gui=light',
		'dl_later='+encodeURIComponent(realHref(href)),
		'tmp_repository_id='+ajxp_bm_repository_id,
		'folder='+ajxp_bm_folder,
        'dl_now='+(jQuery('#ajxp_dl_now')[0].checked ? "true":"false")
	];
	jQuery('#ajxp_bm_iframe').attr("src", ajxp_bm_target+"?" + params.join("&"));
	window.setTimeout(function(){
		jQuery('#ajxp_bm_frame_div').slideUp();
	}, 10000);				
}
function triggerOriginalDL(){
	jQuery("#ajxp_bm_link_menu").slideUp();
	var href = currentLink.attr("href");
	if(currentLink.attr("src")){
		href = currentLink.parents('a').first().attr("href");
	}
	document.location.href = href;	
}
function realHref(href){
	var path = jQuery("<div style=\"background-image:url('"+href+"');\"></div>").css("background-image");
	if (path.indexOf("url(" == 0)) { path = path.substring(4); }
	if (path.lastIndexOf(")") === path.length-1) { path = path.substring(0, path.length - 1); }
	if (path.indexOf("\"") === 0) { path = path.substring(1, path.length); }
	if (path.lastIndexOf("\"") === path.length-1) { path = path.substring(0, path.length - 1); }	
	return path;
}
if(!window.jQuery){
	var element=document.createElement('scr'+'ipt');
	element.setAttribute('src','https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js?t='+(new Date().getTime()));
	if(document.all){
		element.onreadystatechange = function(){
			if(element.readyState == 'loaded'){
				jQuery.noConflict();
				parseLinks();				
			}
		};
	}else{
		element.onload = function(){
			jQuery.noConflict();
			parseLinks();
		};		
	}
	document.body.appendChild(element);
}else{
	parseLinks();
}