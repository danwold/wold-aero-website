%rebase layout

%for f in blog:
	<h1 style="font-size:70%">
       {{f.date}}
	</h1>       
	
       {{f.text}}
	<hr>
%end


