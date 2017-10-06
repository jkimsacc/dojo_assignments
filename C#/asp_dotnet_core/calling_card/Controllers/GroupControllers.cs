using System;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace YourNamespace.Controllers
{
    public class GroupController : Controller
    {
        [HttpGet]
        [Route("string")]
        public string index(){
            return "Some string";
        }
        [HttpGet]
        [Route("int")]
        public int someint(){
            Random rand = new Random();
            return rand.Next(0,10000);
        }
        [HttpGet]
        [Route("json")]
        public JsonResult somejson(){
            return Json(32132311);
        }
        [HttpGet]
        [Route("template")]
        public IActionResult sometemplate(){
            return View("somehtml");
        }
        [HttpGet]
        [Route("{FirstName}/{LastName}/{Age}/{FavoriteColor}")]
        public JsonResult callingCard(string FirstName, string LastName, int Age, string FavoriteColor){
            var Anonobject = new {
                                FirstName = FirstName,
                                LastName = LastName,
                                Age = Age,
                                FavoriteColor = FavoriteColor,
                            };
            return Json(Anonobject);
        }
    }
}