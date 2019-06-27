from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofiles', '0010_auto_20190421_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlunoAulaUC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LAB', 'Laboratorial'), ('P', 'Pratica'), ('T', 'Teorica'), ('TP', 'Teorico-Pratica')], max_length=3)),
                ('horaINI', models.TimeField()),
                ('horaFIM', models.TimeField()),
                ('diaSemana', models.CharField(choices=[('Seg', 'Segunda'), ('Ter', 'Terça'), ('Qua', 'Quarta'), ('Qui', 'Quinta'), ('Sex', 'Sexta'), ('Sab', 'Sabado'), ('Dom', 'Domingo')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('abv', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculdade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoTroca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Aceite', 'Aceite'), ('Recusado', 'Recusado')], default='Pendente', max_length=10)),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Profile')),
                ('aula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('alunoID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Profile')),
                ('aulaID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorAula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aulaID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Aula')),
                ('profID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('abv', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('abv', models.CharField(blank=True, max_length=10, null=True)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('cursoID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Curso')),
            ],
        ),
        migrations.AddField(
            model_name='turno',
            name='ucID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.UnidadeCurricular'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='fac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Faculdade'),
        ),
        migrations.AddField(
            model_name='curso',
            name='dep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Departamento'),
        ),
        migrations.AddField(
            model_name='aula',
            name='turnoID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Turno'),
        ),
        migrations.AddField(
            model_name='alunoaulauc',
            name='aula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.Aula'),
        ),
        migrations.AddField(
            model_name='alunoaulauc',
            name='uc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ucmanage.UnidadeCurricular'),
        ),
    ]
