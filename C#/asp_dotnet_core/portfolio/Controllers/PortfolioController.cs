using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace YourNamespace.Controllers
{
    public class PortfolioController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index(){		
            return View();
        }
        [HttpGet]
        [Route("projects")]
        public IActionResult Project(){		
            return View("projects");
        }
        [HttpGet]
        [Route("contact")]
        public IActionResult Contact(){		
            return View();
        }
    }
}
